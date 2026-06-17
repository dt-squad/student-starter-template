"""
Core encryption utility (AESGCM for randomised, AESGCMSIV for searchable).

See standards/encryption.md for full documentation. Key invariants:
- Searchable encryption uses a fixed nonce -- same plaintext always yields
  the same ciphertext, enabling equality lookups via SQL.
- Non-searchable encryption uses a fresh nonce per call.
- Output is base64(format_type|data_type|nonce+ciphertext) for portability.
"""

import base64
import json
import os
from typing import Any, Optional

import numpy as np
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESGCMSIV

from back_end.utils import pii_data_handlers

ENCRYPTION_KEYS = pii_data_handlers.get_encryption_keys_from_dot_env()
latest_encryption_key, pii_key_id = pii_data_handlers.get_latest_encryption_key_and_id(
    ENCRYPTION_KEYS
)


class EncryptionUtil:
    def __init__(self, pii_key_id, encryption_keys=None, searchable_types=None):
        if not encryption_keys:
            self.encryption_keys = ENCRYPTION_KEYS
        else:
            self.encryption_keys = encryption_keys
        self.key = self.encryption_keys[pii_key_id]
        self.aesgcm = AESGCM(self.encryption_keys[pii_key_id])
        self.aesgcmsiv = AESGCMSIV(self.encryption_keys[pii_key_id])
        if not searchable_types:
            # NOTE: decrypt() chooses AESGCMSIV vs AESGCM by membership here, so
            # EVERY searchable data_type MUST be listed. Crypto.encrypt's temporary
            # add-then-restore trick only fixes the encrypt side; a type missing
            # here encrypts searchable but decrypts non-searchable -> InvalidTag.
            self.searchable_types = {"email", "case_email_address", "file_name", "username"}
        else:
            self.searchable_types = searchable_types
        # TODO: set fixed nonce in .env (matches scaffolding doc)
        self.fixed_nonce = b"\x00" * 12

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(32)

    def _prepare_data(self, data: Any) -> tuple[bytes, str]:
        if data is None:
            return b"null", "none"
        elif isinstance(data, np.ndarray):
            return data.tobytes(), "numpy"
        elif isinstance(data, (dict, list)):
            return json.dumps(data).encode("utf-8"), "json"
        elif isinstance(data, str):
            return data.encode("utf-8"), "string"
        elif isinstance(data, bytes):
            return data, "bytes"
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")

    def _restore_data(self, data: bytes, data_type: str) -> Any:
        if data_type == "none":
            return None
        elif data_type == "numpy":
            return np.frombuffer(data)
        elif data_type == "json":
            return json.loads(data.decode("utf-8"))
        elif data_type == "string":
            return data.decode("utf-8")
        elif data_type == "bytes":
            return data
        else:
            raise ValueError(f"Unknown data type: {data_type}")

    def encrypt(self, data: Any, data_type: str) -> Optional[str]:
        if data is None:
            return None

        data_bytes, format_type = self._prepare_data(data)
        if data_type in self.searchable_types:
            ciphertext = self.aesgcmsiv.encrypt(
                nonce=self.fixed_nonce, data=data_bytes, associated_data=None
            )
        else:
            nonce = os.urandom(12)
            ciphertext = self.aesgcm.encrypt(nonce, data_bytes, None)
            ciphertext = nonce + ciphertext

        return base64.b64encode(
            f"{format_type}|{data_type}|".encode() + ciphertext
        ).decode("utf-8")

    def decrypt(self, encrypted_data: Optional[str]) -> Any:
        if encrypted_data is None:
            return None

        try:
            decoded = base64.b64decode(encrypted_data.encode("utf-8"))
            format_type, data_type, data = decoded.split(b"|", 2)
            format_type = format_type.decode()
            data_type = data_type.decode()

            if format_type not in {"numpy", "json", "string", "bytes", "none"}:
                raise ValueError(f"Invalid format type: {format_type}")

            if data_type in self.searchable_types:
                decrypted = self.aesgcmsiv.decrypt(
                    nonce=self.fixed_nonce, data=data, associated_data=None
                )
            else:
                nonce, ciphertext = data[:12], data[12:]
                decrypted = self.aesgcm.decrypt(nonce, ciphertext, None)

            return self._restore_data(decrypted, format_type)

        except InvalidTag:
            raise ValueError("Decryption failed: Invalid key or corrupted data")
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

    def encrypt_binary(self, data: Optional[bytes]) -> Optional[bytes]:
        """Encrypt raw bytes without base64 / metadata wrapping."""
        if data is None:
            return None
        if not isinstance(data, bytes):
            raise ValueError(f"Expected bytes but got {type(data)}")

        nonce = os.urandom(12)
        ciphertext = self.aesgcm.encrypt(nonce, data, None)
        return nonce + ciphertext

    def decrypt_binary(self, encrypted_data: Optional[bytes]) -> Optional[bytes]:
        if encrypted_data is None:
            return None
        try:
            if not isinstance(encrypted_data, bytes):
                raise ValueError(f"Expected bytes but got {type(encrypted_data)}")

            nonce, ciphertext = encrypted_data[:12], encrypted_data[12:]
            return self.aesgcm.decrypt(nonce, ciphertext, None)

        except InvalidTag:
            raise ValueError("Decryption failed: Invalid key or corrupted data")
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

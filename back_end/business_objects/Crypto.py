"""Singleton wrapper around EncryptionUtil for app-wide encryption use."""

from typing import Any, Optional

from back_end.business_objects.EncryptionUtil import EncryptionUtil
from back_end.utils import pii_data_handlers

ENCRYPTION_KEYS = pii_data_handlers.get_encryption_keys_from_dot_env()


class Crypto:
    def __init__(self):
        self.encryption_keys = ENCRYPTION_KEYS
        self.utils: dict[int, EncryptionUtil] = {}  # key_id -> EncryptionUtil cache

    def _get_util(self, pii_key_id: int) -> EncryptionUtil:
        if pii_key_id not in self.utils:
            self.utils[pii_key_id] = EncryptionUtil(
                pii_key_id, encryption_keys=self.encryption_keys
            )
        return self.utils[pii_key_id]

    def get_latest_key_id(self) -> int:
        return len(self.encryption_keys) - 1

    def encrypt(
        self,
        pii_key_id: int,
        data: Any,
        searchable: bool = False,
        data_type: str = "generic",
    ) -> Optional[str]:
        util = self._get_util(pii_key_id)
        if searchable and data_type not in util.searchable_types:
            original_types = util.searchable_types.copy()
            util.searchable_types.add(data_type)
            result = util.encrypt(data, data_type)
            util.searchable_types = original_types
            return result
        return util.encrypt(data, data_type)

    def decrypt(self, pii_key_id: int, encrypted_data: Optional[str]) -> Any:
        return self._get_util(pii_key_id).decrypt(encrypted_data)

    def encrypt_binary(self, pii_key_id: int, data: Optional[bytes]) -> Optional[bytes]:
        return self._get_util(pii_key_id).encrypt_binary(data)

    def decrypt_binary(
        self, pii_key_id: int, encrypted_data: Optional[bytes]
    ) -> Optional[bytes]:
        return self._get_util(pii_key_id).decrypt_binary(encrypted_data)


# Singleton -- import this everywhere encryption is needed
crypto = Crypto()

"""Encryption key + application-secret utilities.

The two secrets handled here -- ENCRYPTION_KEYS and APPLICATION_SECRET --
deliberately never touch disk anywhere except inside `.env`. Their only
consumer is the running Python process; persisting them to
`secrets_no_git/*.txt` would just enlarge the attack surface without adding
a use case (cf. POSTGRES_PASSWORD, which docker-compose mounts as a secret
file -- different requirement).

Bootstrap flow:

    python3 -m back_end.utils.pii_data_handlers

prints the two lines verbatim; paste them into `.env`.

`settings` is imported lazily inside the loader functions (not at module
top) so this generator runs successfully on a fresh checkout where the
required env vars haven't been populated yet.
"""

import base64
import json
import os


def get_encryption_keys_from_dot_env() -> list[bytes]:
    """Decode the ENCRYPTION_KEYS JSON array into raw key bytes (oldest -> newest)."""
    from back_end.utils.config import settings

    keys_str = json.loads(settings.ENCRYPTION_KEYS)
    return [base64.b64decode(key) for key in keys_str]


def get_latest_encryption_key_and_id(
    encryption_keys: list[bytes],
) -> tuple[bytes, int]:
    if not encryption_keys:
        raise ValueError("No encryption keys configured")
    latest_key_id = len(encryption_keys) - 1
    return encryption_keys[latest_key_id], latest_key_id


def generate_encryption_key() -> str:
    """Fresh base64-encoded 32-byte (AES-256) key. One entry in ENCRYPTION_KEYS."""
    return base64.b64encode(os.urandom(32)).decode("ascii")


def generate_application_secret() -> str:
    """Fresh base64-encoded 48-byte secret for JWT signing (APPLICATION_SECRET)."""
    return base64.b64encode(os.urandom(48)).decode("ascii")


if __name__ == "__main__":
    print(f'ENCRYPTION_KEYS=["{generate_encryption_key()}"]')
    print(f"APPLICATION_SECRET={generate_application_secret()}")

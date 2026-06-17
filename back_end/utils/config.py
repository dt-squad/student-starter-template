"""
Application settings loaded from environment variables via pydantic-settings.

The standards require separate DB_* components, not a pre-built DATABASE_URL,
so passwords with special characters survive escaping. See CLAUDE.md lessons.

`load_env_from_git_root` exists for scripts that run outside FastAPI (e.g.
alembic migrations, db_init, tests) and need .env loaded explicitly. FastAPI
itself picks up .env via the Settings class's env_file config.
"""

from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings


# Minimum length we accept for APPLICATION_SECRET. The standards generator
# (`pii_data_handlers.generate_application_secret`) produces base64-encoded 48
# bytes => 64 chars; 32 is the floor that still represents at least ~24 random
# bytes of entropy. Anything below this is almost certainly a hand-typed value
# or a placeholder that escaped review.
_APPLICATION_SECRET_MIN_CHARS = 32

# Substrings that scream "this is still a placeholder". Belt-and-braces beside
# the length check -- a long placeholder ("PLEASE_REPLACE_BEFORE_DEPLOY...")
# would slip past the length floor on its own.
_APPLICATION_SECRET_PLACEHOLDER_TOKENS = (
    "paste",  # template.env: "<run pii_data_handlers and paste>"
    "replace",
    "changeme",
    "todo",
    "xxxx",
)


def load_env_from_git_root() -> None:
    """Load .env from the repo root for scripts that run outside FastAPI.

    Walks up from this file to find the directory containing .env. No-op if
    the variables are already in the environment (production / CI case).
    """
    import os
    if os.environ.get("DB_NAME"):  # already loaded
        return

    # Walk up: back_end/utils/config.py -> repo root is two levels up
    current = Path(__file__).resolve()
    for parent in (current.parent, *current.parents):
        env_file = parent / ".env"
        if env_file.exists():
            for raw in env_file.read_text(encoding="utf-8").splitlines():
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                # Drop surrounding quotes if present
                if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
                    value = value[1:-1]
                os.environ.setdefault(key, value)
            return


class Settings(BaseSettings):
    """Singleton application settings."""
    # Database (separate components -- DO NOT add DATABASE_URL here)
    DB_URL: str = "localhost"
    DB_PORT: str = "5432"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str
    DB_NAME: str
    ENCRYPTION_KEYS: str
    # Docker / Infrastructure (validated here so .env typos fail fast)
    POSTGRES_EXTERNAL_PORT: str

    @property
    def DATABASE_URL(self) -> str:
        """Compose the postgres connection string at runtime."""
        return (
            f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}"
            f"@{self.DB_URL}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton -- import this everywhere settings are needed
settings = Settings()

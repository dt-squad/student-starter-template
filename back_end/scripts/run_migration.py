"""
Database migration helper script.

Usage:
    python3 -m back_end.scripts.run_migration create -m "Add user table"
    python3 -m back_end.scripts.run_migration upgrade
    python3 -m back_end.scripts.run_migration downgrade
    python3 -m back_end.scripts.run_migration history
    python3 -m back_end.scripts.run_migration current
    python3 -m back_end.scripts.run_migration stamp
"""

import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root.parent))

from back_end.utils.config import load_env_from_git_root
load_env_from_git_root()

from alembic import command
from alembic.config import Config


def get_alembic_config():
    alembic_cfg = Config(os.path.join(project_root, "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(project_root / "migrations"))
    return alembic_cfg


def create_migration(message="New migration"):
    alembic_cfg = get_alembic_config()
    try:
        command.revision(alembic_cfg, autogenerate=True, message=message)
        print(f"Created migration: {message}")
        print("\nREMEMBER: Review the generated migration file before applying!")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def upgrade_db():
    print("Upgrading database...")
    alembic_cfg = get_alembic_config()
    try:
        command.upgrade(alembic_cfg, "head")
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def downgrade_db(target="-1"):
    print(f"Downgrading to: {target}...")
    alembic_cfg = get_alembic_config()
    try:
        command.downgrade(alembic_cfg, target)
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def show_history():
    alembic_cfg = get_alembic_config()
    command.history(alembic_cfg, verbose=True)


def show_current():
    alembic_cfg = get_alembic_config()
    command.current(alembic_cfg, verbose=True)


def stamp_db(revision="head"):
    print(f"Stamping database: {revision}...")
    alembic_cfg = get_alembic_config()
    try:
        command.stamp(alembic_cfg, revision)
        print("Done. Future migrations will apply on top of this baseline.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["create", "upgrade", "downgrade", "history", "current", "stamp"])
    parser.add_argument("-m", "--message", default="New migration")
    parser.add_argument("-t", "--target", default="-1")
    parser.add_argument("-r", "--revision", default="head")

    args = parser.parse_args()

    if args.action == "create":
        create_migration(args.message)
    elif args.action == "upgrade":
        upgrade_db()
    elif args.action == "downgrade":
        downgrade_db(args.target)
    elif args.action == "history":
        show_history()
    elif args.action == "current":
        show_current()
    elif args.action == "stamp":
        stamp_db(args.revision)

import sys
from pathlib import Path

# Project root on path so back_end imports work when run as a script
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from back_end.database.database import SessionLocal
from back_end.database.models import Role


def add_roles(db):
    """Single role for this single-developer internal tool. The Role table +
    FK are kept (scaffold standard; later features assume the role infra
    exists) but only `super user` is seeded, since every protected endpoint
    gates on it and nothing authorizes against `support`/`user`."""
    default_roles = [
        {"name": "super user", "level": 100},
    ]

    for role_data in default_roles:
        existing = db.query(Role).filter_by(name=role_data["name"]).first()
        if not existing:
            role = Role(**role_data)
            db.add(role)
            print(f"  Added role: {role_data['name']} (level {role_data['level']})")
        else:
            print(f"  Role exists: {role_data['name']}")

    db.commit()

def main():
    print("=" * 50)
    print("Database seed (data only)")
    print("=" * 50)

    db = SessionLocal()
    try:

        print("\nAdding roles...")
        add_roles(db)

    finally:
        db.close()


if __name__ == "__main__":
    main()
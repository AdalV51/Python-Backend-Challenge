from sqlalchemy.orm import Session
from app.models import (
    Todo,
    TodoItem,
)  # Update this import as per your project structure
from app.database import (
    SessionLocal,
    engine,
)  # Update these imports as per your project structure


def delete_all_records(db: Session):
    db.query(TodoItem).delete()
    db.query(Todo).delete()
    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    delete_all_records(db)

import random
import datetime

from sqlalchemy.orm import Session

from app import models
from app.models import Todo, TodoItem
from app.database import SessionLocal, engine


def create_todos(db: Session, count: int, due_date: bool = False):
    for i in range(count):
        todo = Todo(title=f"Todo {i}", description=f"Description for Todo {i}")

        if due_date:
            random_days = random.randint(1, 100)
            todo.due_date = datetime.datetime.now() + datetime.timedelta(days=random_days)

        db.add(todo)
        db.commit()
        db.refresh(todo)

        for j in range(5):  # Each Todo will have 5 items
            item = TodoItem(
                title=f"Item {j} of Todo {i}",
                description=f"Description for Item {j} of Todo {i}",
                todo_id=todo.id,
            )

            db.add(item)
            db.commit()


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    create_todos(db, count=100, due_date=True)

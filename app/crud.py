import sqlalchemy
from sqlalchemy.orm import Session

from . import models, schemas


# Todo
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todo_by_title(db: Session, title: str):
    return db.query(models.Todo).filter(models.Todo.title == title).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo_item(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo_by_id(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo


# TodoItem
def get_todo_item_by_id(db: Session, todo_item_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_item_id).first()


def get_todo_items(db: Session, todo_id: int = None):
    if todo_id is None:
        return db.query(models.TodoItem).all()
    else:
        return (
            db.query(models.TodoItem).filter(models.TodoItem.todo_id == todo_id).all()
        )


def create_todo_item(db: Session, todo_item: schemas.TodoItemCreate):
    db_todo_item = models.TodoItem(
        title=todo_item.title,
        description=todo_item.description,
        todo_id=todo_item.todo_id,
    )
    db.add(db_todo_item)
    db.commit()
    db.refresh(db_todo_item)
    return db_todo_item


def update_todo_item_by_id(
    db: Session, todo_item_id: int, todo_item: schemas.TodoItemUpdate
):
    db_todo_item = (
        db.query(models.TodoItem).filter(models.TodoItem.id == todo_item_id).first()
    )
    db_todo_item.title = todo_item.title
    db_todo_item.description = todo_item.description
    db_todo_item.todo_id = todo_item.todo_id
    db.commit()
    db.refresh(db_todo_item)
    return db_todo_item


def delete_todo_item_by_id(db: Session, todo_item_id: int):
    db_todo_item = (
        db.query(models.TodoItem).filter(models.TodoItem.id == todo_item_id).first()
    )
    db.delete(db_todo_item)
    db.commit()
    return db_todo_item


def delete_todo_by_id(db: Session, todo_id: int):
    db_todo_item = (
        db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    )
    db.delete(db_todo_item)
    db.commit()
    return db_todo_item


def get_todo_ordered(db: Session, ordered_by: str):
    column_order = {
        "date": models.Todo.due_date,
        "title": models.Todo.title
    }

    if ordered_by in column_order:
        return db.query(models.Todo).order_by(sqlalchemy.desc(column_order[ordered_by])).all()

    return []

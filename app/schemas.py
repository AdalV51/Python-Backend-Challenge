from datetime import date
from typing import Optional

from pydantic import BaseModel


# Schema for Todo


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoDelete(TodoBase):
    pass


class TodoBaseInDB(TodoBase):
    id: int

    class Config:
        orm_mode = True


class Todo(TodoBaseInDB):
    pass


# Schemas for TodoItem


class TodoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    todo_id: int


class TodoItemCreate(TodoItemBase):
    pass


class TodoItemUpdate(TodoItemBase):
    pass


class TodoItemDelete(TodoItemBase):
    pass


class TodoItemBaseInDB(TodoItemBase):
    id: int

    class Config:
        orm_mode = True


class TodoItem(TodoItemBaseInDB):
    pass

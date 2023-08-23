from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    due_date = Column(Date)

    items = relationship("TodoItem", back_populates="todo")


class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    todo_id = Column(Integer, ForeignKey("todos.id"))

    todo = relationship("Todo", back_populates="items")

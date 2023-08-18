from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create the app
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create the endpoints
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Create a todo
@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_title(db, title=todo.title)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already registered")
    return crud.create_todo_item(db=db, todo=todo)


# Get all todos
@app.get("/todos/", response_model=List[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos


# Get a todo by id
@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


# Update a todo by id
@app.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo_by_id(
    todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)
):
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo_by_id(db=db, todo_id=todo_id, todo=todo)


# Delete a todo by id
@app.delete("/todos/{todo_id}", response_model=schemas.Todo)
def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.delete_todo_by_id(db=db, todo_id=todo_id)


# Create a todo item
@app.post("/todos/{todo_id}/items/", response_model=schemas.TodoItem)
def create_todo_item(
    todo_id: int, todo_item: schemas.TodoItemCreate, db: Session = Depends(get_db)
):
    db_todo_item = crud.get_todo_item_by_title(db, title=todo_item.title)
    if db_todo_item:
        raise HTTPException(status_code=400, detail="Todo item already registered")
    return crud.create_todo_item(db=db, todo_item=todo_item)


# Get all todo items
@app.get("/todos/items/", response_model=List[schemas.TodoItem])
def read_todo_item_ids(db: Session = Depends(get_db)):
    todo_item_ids = crud.get_todo_items(db)
    return todo_item_ids


# Get all todo items from a todo
@app.get("/todos/{todo_id}/items/", response_model=List[schemas.TodoItem])
def read_todo_item_ids(todo_id: int, db: Session = Depends(get_db)):
    todo_item_ids = crud.get_todo_items(db, todo_id=todo_id)
    return todo_item_ids


# Get a todo item by id
@app.get("/todos/items/{todo_item_id}", response_model=schemas.TodoItem)
def read_todo_item_by_id(todo_item_id: int, db: Session = Depends(get_db)):
    db_todo_item = crud.get_todo_item_by_id(db, todo_item_id=todo_item_id)
    if db_todo_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return db_todo_item


# Update a todo item by id
@app.put("/todos/items/{todo_item_id}", response_model=schemas.TodoItem)
def update_todo_item_by_id(
    todo_item_id: int, todo_item: schemas.TodoItemUpdate, db: Session = Depends(get_db)
):
    db_todo_item = crud.get_todo_item_by_id(db, todo_item_id=todo_item_id)
    if db_todo_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return crud.update_todo_item_by_id(
        db=db, todo_item_id=todo_item_id, todo_item=todo_item
    )


# Delete a todo item by id
@app.delete("/todos/items/{todo_item_id}", response_model=schemas.TodoItem)
def delete_todo_item_by_id(todo_item_id: int, db: Session = Depends(get_db)):
    db_todo_item = crud.get_todo_item_by_id(db, todo_item_id=todo_item_id)
    if db_todo_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return crud.delete_todo_item_by_id(db=db, todo_item_id=todo_item_id)

# Adding some cool changes!

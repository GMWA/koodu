from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from todo.dependencies import get_db
from todo.models import Todo as TodoModel
from todo.schemas.todos import Todo as TodoSchema
from todo.schemas.todos import TodoCreate

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[TodoSchema],
    responses={403: {"description": "Operation forbidden"}},
)
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(TodoModel).all()
    return list(map(lambda cat: cat.to_dict(), categories))


@router.get(
    "/{todo_id}",
    response_model=TodoSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter_by(id=todo_id).first()
    if not todo:
        raise HTTPException(404, "todo Not Found!")
    else:
        return todo.to_dict()


@router.post(
    "/",
    response_model=TodoSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    try:
        todo = db.query(TodoModel).filter_by(name=todo.name).first()
        if todo:
            raise HTTPException(400, "todo already exists")
        db_todo = TodoModel(**todo.dict())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo.to_dict()
    except Exception as exc:
        raise HTTPException(500, f"Server Error {exc}!")
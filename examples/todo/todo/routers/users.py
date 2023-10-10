from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from todo.dependencies import get_db
from todo.models import User as UserModel
from todo.schemas.users import User as UserSchema
from todo.schemas.users import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[UserSchema],
    responses={403: {"description": "Operation forbidden"}},
)
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(UserModel).all()
    return list(map(lambda cat: cat.to_dict(), categories))


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(404, "user Not Found!")
    else:
        return user.to_dict()


@router.post(
    "/",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter_by(name=user.name).first()
        if user:
            raise HTTPException(400, "user already exists")
        db_user = UserModel(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user.to_dict()
    except Exception as exc:
        raise HTTPException(500, f"Server Error {exc}!")
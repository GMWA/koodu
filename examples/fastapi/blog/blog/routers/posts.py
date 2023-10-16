from typing import List

from blog.dependencies import get_db
from blog.models import Post as PostModel
from blog.schemas.posts import Post as PostSchema
from blog.schemas.posts import PostCreate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[PostSchema],
    responses={403: {"description": "Operation forbidden"}},
)
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(PostModel).all()
    return list(map(lambda cat: cat.to_dict(), categories))


@router.get(
    "/{post_id}",
    response_model=PostSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter_by(id=post_id).first()
    if not post:
        raise HTTPException(404, "post Not Found!")
    else:
        return post.to_dict()


@router.post(
    "/",
    response_model=PostSchema,
    responses={403: {"description": "Operation forbidden"}},
)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    try:
        post = db.query(PostModel).filter_by(name=post.name).first()
        if post:
            raise HTTPException(400, "post already exists")
        db_post = PostModel(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post.to_dict()
    except Exception as exc:
        raise HTTPException(500, f"Server Error {exc}!")

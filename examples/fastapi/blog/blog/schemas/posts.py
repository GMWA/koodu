from typing import Union
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str
    user_id: int


class PostCreate(PostBase):
    pass


class UpdatePost(PostBase):
    id: int
    pass


class Post(PostBase):
    id: int
    title: str
    text: str
    user_id: int

    class Config:
        orm_mode = True
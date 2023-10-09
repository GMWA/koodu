from typing import Union
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    description: Union[str, None] = None
    pass


class UpdateCategory(CategoryBase):
    id: int
    description: Union[str, None] = None
    pass


class Category(CategoryBase):
    id: int
    name: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True
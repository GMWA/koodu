from typing import Union

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    category_id: int
    user_id: int


class TodoCreate(TodoBase):
    description: Union[str, None] = None
    pass


class UpdateTodo(TodoBase):
    id: int
    description: Union[str, None] = None
    pass


class Todo(TodoBase):
    id: int
    title: str
    description: Union[str, None] = None
    category_id: int
    user_id: int

    class Config:
        orm_mode = True

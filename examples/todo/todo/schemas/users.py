from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UpdateUser(UserBase):
    id: int
    pass


class User(UserBase):
    id: int
    name: str
    email: str
    username: str
    password: str

    class Config:
        orm_mode = True

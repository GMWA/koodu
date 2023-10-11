from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from todo.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    description = Column(Text(1000))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text(1000))
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

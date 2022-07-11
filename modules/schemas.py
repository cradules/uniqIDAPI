from typing import List, Union
import datetime as _dt

from pydantic import BaseModel


class ItemBase(BaseModel):
    projectID: str
    projectUID: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    registration_date: _dt.datetime
    last_update: _dt.datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

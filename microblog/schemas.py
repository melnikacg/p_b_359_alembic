from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str


class PostList(BaseModel):
    id: int
    date: datetime

    class Config:
        orm_mode = True

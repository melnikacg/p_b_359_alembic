from sqlalchemy import Column, String, Integer, Text, DateTime
from core.db import Base


class Post(Base):
    __tablename__ = "microblog_posts"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text(350))
    date = Column(DateTime)


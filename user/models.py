from sqlalchemy import Column, String, Integer, DateTime, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.db import Base


#class UserTable(Base, SQLAlchemyBaseUserTable):
#    __tablename__ = "user_table"
    #uvicorn main:app --reloadpass
#    name = Column(String, unique=True)
#    date = Column(DateTime)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, ForeignKey,text
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    """
    User class

    Args:
        Base (sqlalchemy.ext.declarative.api.Base): Base class
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default= text('now()'))
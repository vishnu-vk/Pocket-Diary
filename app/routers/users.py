from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from typing import List

from ..schemas import user_schema
from ..database import get_db
from ..api import users

router = APIRouter(
    prefix= "/users",
    tags= ["Users"]
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model= user_schema.UserResponse)
def create_users(request: user_schema.UserCreate, db: Session = Depends(get_db)):
    return users.create_user(request, db)

@router.get("/{id}", response_model= user_schema.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return users.get_user(id, db)


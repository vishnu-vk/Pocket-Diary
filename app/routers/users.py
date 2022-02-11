from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import user_schema
from app.database import get_db
from app.models import User
from app.utils import hash

router = APIRouter(
    prefix= "/users",
    tags= ["Users"]
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model= user_schema.UserResponse)
def create_users(request: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user

    Args:
        request (schemas.UserCreate): User data
        db (Session): Database session

    Returns:
        models.User: User created
    """

    if db.query(User).filter(User.email == request.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User wiht email id {request.email} already exists")
    
    request.password = hash(request.password)

    new_user = User(**request.dict())
        
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 

    return new_user


@router.get("/{id}", response_model= user_schema.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    """
    Sent a individual user

    Args:
        id (int): User id
        db (Session): Database session

    Raises:
        HTTPException: User not found

    Returns:
        models.User: User found
    """

    user = db.query(User).filter(User.user_id == id).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"user with id {id} was not found")
    
    return user


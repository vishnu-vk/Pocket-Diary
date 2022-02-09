from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import user_schema
from ..utils import hash

def create_user(input_data: user_schema.UserCreate, db: Session):
    """
    Create a new user

    Args:
        request (schemas.UserCreate): User data
        db (Session): Database session

    Returns:
        models.User: User created
    """

    if db.query(User).filter(User.email == input_data.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User wiht email id {input_data.email} already exists")

    input_data.password = hash(input_data.password)

    new_user = User(**input_data.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 

    return new_user


def get_user(id: int, db: Session):
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
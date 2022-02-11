from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from app.models import User 
from app.schemas import token_shema
from app.database import get_db
from app.utils import verify
from app.oauth2 import create_access_token

router = APIRouter(
    tags= ["Authentication"]
)

@router.post("/login", response_model= token_shema.AccessToken)
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    User login

    Args:
        db (Session): Database session
        user_credentials (OAuth2PasswordRequestForm): login details

    Returns:
        : access token created
    """

    user = db.query(User).filter(User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Invalid credentials")
    
    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Invalid credentials")

    access_token = token_shema.AccessToken(access_token= create_access_token(data= {"user_id": user.user_id}), token_type= "bearer")

    return access_token

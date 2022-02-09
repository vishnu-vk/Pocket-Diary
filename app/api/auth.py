from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import token_shema

from ..models import User
from ..utils import verify
from ..oauth2 import create_access_token

def user_login(db: Session, user_credentials: OAuth2PasswordRequestForm = Depends()):
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



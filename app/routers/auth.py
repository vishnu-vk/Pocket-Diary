from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from ..models import User 
from ..schemas import token_shema
from ..database import get_db
from ..utils import *
from ..oauth2 import *
from ..api import auth

router = APIRouter(
    tags= ["Authentication"]
)

@router.post("/login", response_model= token_shema.AccessToken)
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.user_login(db, user_credentials)

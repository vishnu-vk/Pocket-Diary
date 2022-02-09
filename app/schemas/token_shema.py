from typing import Optional
from pydantic import BaseModel

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class Token(BaseModel):
    id: Optional[str] = None
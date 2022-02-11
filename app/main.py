from fastapi import FastAPI
# from config import settings
from app.models import Base
from app.database import engine
from app.routers import transactions, users, auth
from fastapi.middleware.cors import CORSMiddleware 
 

app = FastAPI()

# origins = ['*']

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins= origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
# app.include_router(votes.router)



@app.get("/")
def root():
    return {"message": "welcome"}
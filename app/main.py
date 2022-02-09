from fastapi import FastAPI
# from config import settings
from .models import Base
from .database import engine
from .routers import transactions, users, auth
# from fastapi.middleware.cors import CORSMiddleware 
 

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

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
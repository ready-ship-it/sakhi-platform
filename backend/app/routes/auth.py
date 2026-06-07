from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.utils.security import create_token

router = APIRouter()

def db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()

users = []

<<<<<<< HEAD
@router.post("/register")
def register(email: str, password: str):
    users.append({"email": email, "password": password})
    return {"message": "registered"}

@router.post("/login")
def login(email: str, password: str):
    for u in users:
        if u["email"] == email and u["password"] == password:
            return {"token": create_token(1)}
    return {"error": "invalid"}
=======
from app.schemas.auth import RegisterRequest

@router.post("/register")
def register(data: RegisterRequest):

    email = data.email
    password = data.password

    return {"message": "registered"}

from app.schemas.auth import LoginRequest

@router.post("/login")
def login(data: LoginRequest):

    email = data.email
    password = data.password

    return {"token": "example"}
>>>>>>> 1bdb669 (Initial commit: new)

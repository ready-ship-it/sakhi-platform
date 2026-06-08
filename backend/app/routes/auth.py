from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.database import get_db
from app.models.user import User

router = APIRouter()


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing:
        return {
            "success": False,
            "message": "Email already registered"
        }

    user = User(
        email=data.email,
        password=data.password
    )

    db.add(user)
    db.commit()

    return {
        "success": True,
        "message": "User registered successfully"
    }


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == data.email,
        User.password == data.password
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    return {
        "success": True,
        "message": "Login successful",
        "email": user.email
    }
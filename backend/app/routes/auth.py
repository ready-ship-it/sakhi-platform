from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext

from app.database import get_db
from app.models.user import User

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


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

    hashed_password = pwd_context.hash(
        data.password
    )

    user = User(
        email=data.email,
        password=hashed_password
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
        User.email == data.email
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    if not pwd_context.verify(
        data.password,
        user.password
    ):
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    return {
        "success": True,
        "message": "Login successful",
        "email": user.email
    }
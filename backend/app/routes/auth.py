from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

# Temporary in-memory users
users = []


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
def register(data: RegisterRequest):

    # Check if user exists
    for user in users:
        if user["email"] == data.email:
            return {
                "success": False,
                "message": "Email already registered"
            }

    users.append({
        "email": data.email,
        "password": data.password
    })

    return {
        "success": True,
        "message": "User registered successfully"
    }


@router.post("/login")
def login(data: LoginRequest):

    for user in users:
        if (
            user["email"] == data.email
            and user["password"] == data.password
        ):
            return {
                "success": True,
                "message": "Login successful",
                "email": data.email
            }

    return {
        "success": False,
        "message": "Invalid credentials"
    }
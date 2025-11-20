from typing import Optional, List
from pydantic import BaseModel


# ===== AUTH – REQUESTY OD ANDROIDA =====

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str

class LoginRequest(BaseModel):
    email: str
    password: str

# ===== AUTH – ODPOWIEDZI DO ANDROIDA (dopasowane do ApiModels.kt) =====
class LoginResponse(BaseModel):
    token: str
    userId: str
    message: Optional[str] = None


class RegisterResponse(BaseModel):
    token: str
    userId: str
    message: Optional[str] = None


# ===== PHOTO – ODPOWIEDŹ PO UPLOADZIE (dopasowane do ApiModels.kt) =====
class PhotoUploadResponse(BaseModel):
    photoId: str
    url: str
    message: str

class ApiError(BaseModel):
    error: str
    message: str


# ===== UŻYTKOWNIK – WEWNĘTRZNE SCHEMATY =====
class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

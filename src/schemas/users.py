import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UsersInfo(schemas.BaseUser[uuid.UUID]):
    name: str
    phone_number: str
    is_client: bool


class CreateUserSchema(schemas.BaseUserCreate):
    name: str
    phone_number: str
    is_client: bool = True
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UpdateUserSchema(schemas.BaseUserUpdate):
    name: str
    phone_number: str
    is_client: bool = True
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None

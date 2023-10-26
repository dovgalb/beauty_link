import uuid
from typing import List
from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from src.auth.jwt import auth_backend
from src.db.managers import get_user_manager
from src.db.models import User
from src.repository.filter.users import UsersFilter, users_filter
from src.schemas.users import UsersInfo, CreateUserSchema, UpdateUserSchema

from src.services.users import users_service

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

users_router = APIRouter()

users_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)

users_router.include_router(
    fastapi_users.get_register_router(UsersInfo, CreateUserSchema),
    prefix="/auth",
    tags=["auth"],
)


@users_router.get('/', response_model=list[UsersInfo])
async def get_users(
        service=Depends(users_service),
        query_filter: UsersFilter = Depends(users_filter)
):
    return await service._list(query_filter)


@users_router.put('/{user_id}', response_model=UpdateUserSchema)
async def update_users(
        user_id: int,
        data: UpdateUserSchema,
        service=Depends(users_service)
):
    return await service._update(data=data, entity_id=user_id)



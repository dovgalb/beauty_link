from typing import List
from fastapi import APIRouter, Depends


users_router = APIRouter()


@users_router.get('/{user_id}')
async def get_test(user_id: int):
    return user_id
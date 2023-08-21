from typing import List
from fastapi import APIRouter, Depends

from src.schemas.services import ServicesInfo, CreateServiceScheme, UpdateServiceScheme
from src.services.services import services_service
from src.repository.filter.services import services_filter

services_router = APIRouter()


@services_router.get('/', response_model=list[ServicesInfo])
async def get_services(
        service=Depends(services_service)
):
    """Получение списка услуг"""
    return await service._list(services_filter)


@services_router.post('/', response_model=CreateServiceScheme)
async def create_service(
        data: CreateServiceScheme,
        service=Depends(services_service)
):
    return await service._create(data)

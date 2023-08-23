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
    """Создание услуги"""
    return await service._create(data)


@services_router.put('/{service_id}', response_model=UpdateServiceScheme)
async def update_service(
        service_id: int,
        data: UpdateServiceScheme,
        service=Depends(services_service)

):
    """Обновляет услугу"""
    return await service._update(entity_id=service_id, data=data)


@services_router.delete('/{service_id}')
async def delete_service(
        service_id: int,
        service=Depends(services_service)
):
    return await service._delete(entity_id=service_id)
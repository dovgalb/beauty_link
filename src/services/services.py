"""
Модуль для бизнес логики
"""

from src.repository.crud.services import services_repository
from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.services import ServicesInfo


class ServicesService(CrudService):
    pass


def services_service() -> ServicesService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=services_repository,
    )

    return ServicesService(
        unit_of_work=unit_of_work,
        read_schema=ServicesInfo
    )

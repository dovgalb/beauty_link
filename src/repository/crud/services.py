from src.db.models import Service
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.services import CreateServiceScheme, UpdateServiceScheme


class ServicesRepository(
    SQLAlchemyCRUD[Service, CreateServiceScheme, UpdateServiceScheme]
):
    pass


services_repository = ServicesRepository(Service)

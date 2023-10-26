from src.repository.crud.users import users_repository
from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.users import UsersInfo


class UsersService(CrudService):
    pass


def users_service() -> UsersService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=users_repository,
    )

    return UsersService(
        unit_of_work=unit_of_work,
        read_schema=UsersInfo,
    )
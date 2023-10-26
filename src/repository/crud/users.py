from src.db.models import User
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.users import UsersInfo, CreateUserSchema, UpdateUserSchema


class UsersRepository(
    SQLAlchemyCRUD[User, CreateUserSchema, UpdateUserSchema]
):
    pass


users_repository = UsersRepository(User)
from src.db.models import User
from src.repository.filter.base import SqlAlchemyFilter


class UsersFilter(SqlAlchemyFilter):
    pass


users_filter = UsersFilter(User)
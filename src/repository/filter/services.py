from src.db.models import Service
from src.repository.filter.base import SqlAlchemyFilter


class ServicesFilter(SqlAlchemyFilter):
    pass


services_filter = ServicesFilter(Service)
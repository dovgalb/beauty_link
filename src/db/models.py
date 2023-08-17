from src.db.base import Base
from sqlalchemy.orm import mapped_column, relationship, backref
from sqlalchemy import ForeignKey, String, Integer, Boolean, TIMESTAMP, DateTime


class Master(Base):
    __tablename__ = "masters"

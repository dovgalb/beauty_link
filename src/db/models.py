from src.db.base import Base
from sqlalchemy.orm import mapped_column, relationship, backref, Mapped
from sqlalchemy import ForeignKey, String, Integer, Boolean, TIMESTAMP, DateTime, Time, func
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from src.db.base import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), index=True)
    phone_number = mapped_column(String(20), unique=True)
    is_client = mapped_column(Boolean, nullable=True)

    master = relationship("Master", back_populates="user", uselist=False)
    bookings = relationship("Booking", back_populates='client')


class Master(Base):
    __tablename__ = "masters"

    id = mapped_column(Integer, primary_key=True)
    city = mapped_column(String(50))
    address = mapped_column(String(255))
    start_time = mapped_column(Time)
    end_time = mapped_column(Time)

    services = relationship("Service", back_populates="master")
    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="master")


class Service(Base):
    __tablename__ = 'services'

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(255), index=True)
    description = mapped_column(String(500), nullable=True)
    price = mapped_column(Integer)
    duration = mapped_column(Integer)

    master_id = mapped_column(Integer, ForeignKey('masters.id'))
    master = relationship("Master", back_populates="services")


class Booking(Base):
    __tablename__ = "bookings"

    id = mapped_column(Integer, primary_key=True)
    start_time = mapped_column(DateTime)
    create_time = mapped_column(DateTime, server_default=func.now())
    client_name = mapped_column(String(50), nullable=True)
    phone_number = mapped_column(String(20), nullable=True)
    comment = mapped_column(String(500), nullable=True)

    client_id = mapped_column(ForeignKey("users.id"))
    client = relationship("User", back_populates="bookings")

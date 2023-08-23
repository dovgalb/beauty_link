from typing import Optional

from pydantic import BaseModel


class ServicesInfo(BaseModel):
    """
    Базовая схема для услуг
    """

    id: int
    title: str
    description: Optional[str]
    price: int
    duration: int
    is_active: bool
    master_id: int

    class Config:
        orm_mode = True


class CreateServiceScheme(BaseModel):
    """
    Схема создания услуги
    """

    title: str
    description: Optional[str]
    price: int
    duration: int
    is_active: bool
    master_id: int


class UpdateServiceScheme(BaseModel):
    """
    Схема для обновления Услуги
    """
    title: str
    description: Optional[str]
    price: int
    duration: int
    is_active: bool


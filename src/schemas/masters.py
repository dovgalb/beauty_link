from pydantic import BaseModel

from datetime import time


class MastersInfo(BaseModel):
    """Базовая схема мастеров"""

    id: int
    city: str
    address: str
    start_time: time
    end_time: time
    user_id: int
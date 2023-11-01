import uuid
from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
    UUID4,
)


class _ID(BaseModel):
    id: UUID4 = Field(alias='_id', default=uuid.uuid4())


class _Time(BaseModel):
    # TODO: продумать другие варианты хранения времени
    hour: int = Field(default=0, ge=0, le=23)
    min: int = Field(default=0, ge=0, le=59)


class _Date(BaseModel):
    # TODO: продумать другие варианты хранения даты
    year: int = Field(default=datetime.today().year, ge=datetime.today().year)
    month: int = Field(default=datetime.today().month, ge=datetime.today().month)
    day: int = Field(ge=1, le=31)


class Appointment(_ID):
    event_id: UUID4
    client_id: UUID4 | None = None
    date: _Date
    time: _Time
    # price: float


class Event(_ID):
    title: str
    # description: str
    agent_id: UUID4
    date: _Date
    appointments: list[Appointment] = []
    # type: str
    # status: str


class Client(_ID):
    name: str
    appointments: list[Appointment] = []
    # second_name: str
    # phone_number: str


class Agent(_ID):
    title: str
    events: list[Event] = []
    # rate: float

# from enum import Enum

from pydantic import (
    BaseModel,
    Field,
)


# class Status(str, Enum):
#     FROZEN = "FROZEN"
#     ACTIVE = "ACTIVE"
#     IN_ARCHIVE = "IN_ARCHIVE"

class EventTitle(BaseModel):
    title: str


class EventId(BaseModel):
    id_: int = Field(alias='_id')


class EventBase(BaseModel):
    title: str
    # description: str
    agent_id: int
    # date: str
    # type: str
    # status: Status


class Event(EventId, EventBase):
    pass

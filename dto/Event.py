# from enum import Enum

from pydantic import (
    BaseModel,
    Field,
)


# class Status(str, Enum):
#     FROZEN = "FROZEN"
#     ACTIVE = "ACTIVE"
#     IN_ARCHIVE = "IN_ARCHIVE"


class Event(BaseModel):
    id: int = Field(alias='_id')
    title: str
    # description: str
    agent_id: int
    # type: str
    # lock: bool

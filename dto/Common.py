from typing import List

from pydantic import (
    BaseModel,
    Field,
)

from models.Event import Event


class AgentEvents(BaseModel):
    event_list: List[Event]


class Message(BaseModel):
    ru: str
    en: str

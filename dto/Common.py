from typing import List

from pydantic import (
    BaseModel,
    Field,
)

from models import Event


class AgentEvents(BaseModel):
    # agent_id: int
    event_list: List[Event]


class Message(BaseModel):
    ru: str
    en: str

from typing import List

from pydantic import (
    BaseModel,
)

from dto.Event import (
    Event,
    EventBase,
)


class AgentEvents(BaseModel):
    event_list: List[Event]


class ClientAppointments(BaseModel):
    appointments: List[EventBase]


class Message(BaseModel):
    ru: str
    en: str

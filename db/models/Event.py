from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    # description: str
    agent_id: int
    # date: str
    # type: str
    # status: str

from pydantic import BaseModel


class Agent(BaseModel):
    id: int
    title: str
    # rate: float

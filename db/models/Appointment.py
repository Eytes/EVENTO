from pydantic import (
    BaseModel,
    Field,
)


class Appointment(BaseModel):
    id_: int = Field(alias='_id')
    client_id: int
    event_id: int
    date: str
    # time: str
    # price: float

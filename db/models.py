from pydantic import (
    BaseModel,
    Field,
    UUID4
)


class __ID(BaseModel):
    id: UUID4 = Field(alias='_id')


class __Time(BaseModel):
    time: str


class __Date(BaseModel):
    date: str


class Appointment(__ID, __Date, __Time):
    event_id: UUID4
    # price: float


class ClientAppointment(Appointment):
    client_id: UUID4


class Event(__ID, __Date):
    title: str
    # description: str
    agent_id: UUID4
    # type: str
    # status: str


class Client(__ID):
    name: str
    # second_name: str
    # phone_number: str


class Agent(__ID):
    title: str
    # rate: float

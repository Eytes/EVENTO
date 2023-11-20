from pydantic import (
    BaseModel,
    Field,
)


class AppointmentBase(BaseModel):
    # date: str
    # time: str
    # price: float
    pass


class AppointmentId(BaseModel):
    id_: int = Field(alias='_id')


class AppointmentDependencies(BaseModel):
    event_id: int
    client_id: int


class Appointment(AppointmentId, AppointmentDependencies, AppointmentBase):
    pass

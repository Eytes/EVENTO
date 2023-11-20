from uuid import UUID

from fastapi import FastAPI

from crud import (
    agent as agent_crud,
    client as client_crud,
    appointment as appointment_crud,
    event as event_crud,
)

from models import (
    Event,
    Agent,
    Client,
    Appointment,
    ClientAppointment,
)

app = FastAPI()


@app.get("/events/{event_id}/appointments/")
async def get_event_appointments(event_id: UUID) -> list:
    """ Получение всех записей на событие """
    return appointment_crud.get_by_event_id(event_id)


@app.post("/events/{event_id}/appointments/")
def post_event_appointment(appointment: Appointment) -> str:
    """ Создание возможной записи на событие """
    return appointment_crud.create(appointment)


@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: UUID):
    pass

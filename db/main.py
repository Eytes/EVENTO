from fastapi import FastAPI
from pydantic import UUID4

from crud import (
    AgentCRUD,
    ClientCRUD,
    AppointmentCRUD,
    EventCRUD,
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
async def get_event_appointments(event_id: UUID4) -> list:
    """ Получение всех записей на событие """
    return AppointmentCRUD.get_by_event_id(event_id)


@app.post("/events/{event_id}/appointments/")
def post_event_appointment(appointment: Appointment) -> str:
    """ Создание возможной записи на событие """
    return AppointmentCRUD.create(appointment)


@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: UUID4):
    pass

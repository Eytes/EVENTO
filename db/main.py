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
    pass


@app.post("/events/appointments/")
def create_appointment(appointment: Appointment) -> str:
    """ Создание возможной записи на событие """
    return AppointmentCRUD.create(appointment)


@app.delete("/events/appointments/")
def delete_appointment(event_id: UUID4, appointment_id: UUID4):
    """ Удалить запись на событие """
    AppointmentCRUD.delete(event_id, appointment_id)


@app.put("/events/{event_id}/appointments/{appointment_id}")
def change_appointment(event_id: UUID4, appointment_id: UUID4):
    """ Изменение параметров записи на событие """
    pass

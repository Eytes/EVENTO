from fastapi import FastAPI

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
)

app = FastAPI()


@app.get("/db/appointments/{event_title}")
async def appointments(event_title: str):
    return


@app.post("/db/appointments/")
async def create_appointments(appointment: Appointment):
    return AppointmentCRUD.create(appointment)


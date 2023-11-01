from fastapi import (
    APIRouter,
)
from pydantic import UUID4

from db.crud import AppointmentCRUD
from db.models import Appointment

router = APIRouter(
    prefix='/appointments',
    tags=['Appointments']
)


@router.post("/create")
def create_appointment(appointment: Appointment) -> str:
    """ Создание возможной записи на событие """
    return AppointmentCRUD.create(appointment)


@router.delete("/delete")
def delete_appointment(event_id: UUID4, appointment_id: UUID4):
    """ Удалить запись на событие """
    AppointmentCRUD.delete(event_id, appointment_id)


@router.put("/change")
def change_appointment(event_id: UUID4, appointment_id: UUID4):
    """ Изменение параметров записи на событие """
    pass

from fastapi import (
    APIRouter,
)
from pydantic import UUID4

from db.crud import EventCRUD
from db.models import Event

router = APIRouter(
    prefix='/events',
    tags=['Events']
)


@router.post('/create')
def create_event(event: Event) -> str:
    """ Создание события """
    return EventCRUD.create(event)


@router.get("/get")
def get_event(event_id: UUID4):
    """ Возвращает Event по указанному id """
    return EventCRUD.get_by_id(event_id)


@router.get("/appointments")
async def get_event_appointments(event_id: UUID4) -> list:
    """ Получение всех записей на событие """
    ...

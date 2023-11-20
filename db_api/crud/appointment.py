from uuid import UUID

from db_api.models import Appointment
from db_api.collections import appointments as appointments_collection
from db_api.crud.common import (
    create_document,
    update_document,
    get_document,
)


def make_an_appointment(appointment: Appointment, client_id: UUID) -> None:
    """ Запись клиента на событие  """
    update_document(
        appointments_collection,
        {"_id": appointment.id},
        {"client_id": client_id}
    )


def create(appointment: Appointment) -> str:
    """ Создание записи на событие """
    return create_document(
        appointments_collection,
        appointment.model_dump(by_alias=True)
    )


def get_by_client_id(client_id: UUID) -> list:
    """ Получеение данных о записи клиента """
    return get_document(
        appointments_collection,
        {'client_id': client_id}
    )


def get_by_event_id(event_id: UUID) -> list:
    """ Получеение данных о записи клиента """

    data = get_document(
        appointments_collection,
        {'event_id': event_id},
        multiple=True
    )
    return [Appointment(**item) for item in data]

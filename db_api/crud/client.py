from uuid import UUID

from db_api.models import Client
from db_api.collections import clients as clients_collection
from db_api.crud.common import (
    create_document,
    get_document,
)


def create(client: Client) -> str:
    """ Создание клиента """
    return create_document(
        clients_collection,
        client.model_dump()
    )


def get(client_id: UUID) -> Client:
    """ Получеение данных о клиенте """
    client_data = get_document(
        clients_collection,
        {'_id': client_id}
    )[0]
    client = Client(**client_data)
    return client

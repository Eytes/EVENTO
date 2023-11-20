from db_api.crud.common import (
    create_document,
    get_document,
)
from db_api.models import Event
from db_api.collections import events as events_collection


def create(event: Event) -> str:
    """ Создание события """
    return create_document(
        events_collection,
        event.model_dump()
    )


def get_by_title(title: str) -> list[Event]:
    """ Получение данных о событии """
    data = get_document(
        events_collection,
        {"title": title},
        multiple=True
    )
    return [Event(**item) for item in data]

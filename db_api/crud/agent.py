from db_api.crud.common import (
    create_document,
    get_document,
)
from db_api.models import Agent
from db_api.collections import agents as agents_collection


def create(agent: Agent) -> str:
    """ Создание агента. Агент - представитель и организатор события """
    return create_document(
        agents_collection,
        agent.model_dump()
    )


def get_by_title(title: str) -> list:
    """ Получение данных об агенте """
    return get_document(
        agents_collection,
        {"title": title}
    )

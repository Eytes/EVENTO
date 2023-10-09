from pymongo.collection import Collection

from .Collections import (
    agents,
    events,
    appointments,
    clients
)


def __create_document(collection: Collection, document: dict) -> str:
    """ Function to insert a document into a collection and
    return the document's id. """
    return str(collection.insert_one(document).inserted_id)


def __get_document(collection: Collection, elements: dict, multiple: bool = False) -> list:
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements. """
    if multiple:
        results = collection.find(elements)
    else:
        results = collection.find_one(elements)
    return [r for r in results]


def __update_document(collection: Collection, query_elements: dict, new_values: dict) -> None:
    """ Function to update a single document in a collection. """
    collection.update_one(query_elements, {'$set': new_values})


def __delete_document(collection: Collection, query: dict) -> None:
    """ Function to delete a single document from a collection. """
    collection.delete_one(query)


def create_agent(agent: dict) -> str:
    """ Создание агента. Агент - представитьель и организатор события """
    return __create_document(agents, agent)


def create_event(event: dict) -> str:
    """ Создание события """
    return __create_document(events, event)


def create_appointment(appointment: dict) -> str:
    """ Запись клиента на событие  """
    return __create_document(appointments, appointment)


def create_client(client: dict) -> str:
    """ Создание клиента """
    return __create_document(clients, client)


def get_agent_by_title(title: str) -> list:
    """ Получеение данных о агенте """
    return __get_document(agents, {"title": title})


def get_event_by_title(title: str) -> list:
    """ Получеение данных о событии """
    return __get_document(events, {"title": title}, multiple=True)


def get_client_appointment(client_id: int) -> list:
    """ Получеение данных о записи клиента """
    return __get_document(appointments, {'client_id': client_id})


def get_client(id_: int) -> list:
    """ Получеение данных о клиенте """
    return __get_document(clients, {'_id': id_})

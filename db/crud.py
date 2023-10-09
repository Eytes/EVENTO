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


def __delete_document(collection, query):
    """ Function to delete a single document from a collection. """
    collection.delete_one(query)


def create_agent():
    """ Создание агента. Агент - представитьель и организатор события """
    pass


def create_event():
    """ Создание события """
    pass


def create_appointment():
    """ Запись клиента на событие  """
    pass


def create_client():
    """ Создание клиента """
    pass


def get_agent():
    """ Получеение данных о агенте """
    pass


def get_event():
    """ Получеение данных о событии """
    pass


def get_appointment():
    """ Получеение данных о записи клиента """
    pass


def get_client():
    """ Получеение данных о клиенте """
    pass

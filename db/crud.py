from pymongo.collection import Collection

from Collections import (
    agents,
    events,
    appointments,
    clients
)

from models import (
    Event,
    Agent,
    Client,
    Appointment,
)


class __MongoCRUD:
    @staticmethod
    def create_document(collection: Collection, document: dict) -> str:
        """ Function to insert a document into a collection and
        return the document's id. """
        return str(collection.insert_one(document).inserted_id)

    @staticmethod
    def get_document(collection: Collection, elements: dict, multiple: bool = False) -> list:
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements. """
        if multiple:
            results = collection.find(elements)
        else:
            results = collection.find_one(elements)
        return [r for r in results]

    @staticmethod
    def update_document(collection: Collection, query_elements: dict, new_values: dict) -> None:
        """ Function to update a single document in a collection. """
        collection.update_one(query_elements, {'$set': new_values})

    @staticmethod
    def delete_document(collection: Collection, query: dict) -> None:
        """ Function to delete a single document from a collection. """
        collection.delete_one(query)


class AgentCRUD(__MongoCRUD):
    @staticmethod
    def create(agent: dict) -> str:
        """ Создание агента. Агент - представитьель и организатор события """
        return super().create_document(agents, agent)

    @staticmethod
    def get_by_title(title: str) -> list:
        """ Получеение данных о агенте """
        return super().get_document(agents, {"title": title})


class EventCRUD(__MongoCRUD):
    @staticmethod
    def create(event: dict) -> str:
        """ Создание события """
        return super().create_document(events, event)

    @staticmethod
    def get_by_title(title: str) -> list:
        """ Получеение данных о событии """
        return super().get_document(events, {"title": title}, multiple=True)


class AppointmentCRUD(__MongoCRUD):
    @staticmethod
    def create_appointment(appointment: dict) -> str:
        """ Запись клиента на событие  """
        return super().create_document(appointments, appointment)

    @staticmethod
    def get_client_appointment(client_id: int) -> list:
        """ Получеение данных о записи клиента """
        return super().get_document(appointments, {'client_id': client_id})


class ClientCRUD(__MongoCRUD):
    @staticmethod
    def create_client(client: dict) -> str:
        """ Создание клиента """
        return super().create_document(clients, client)

    @staticmethod
    def get_client(id_: int) -> list:
        """ Получеение данных о клиенте """
        return super().get_document(clients, {'_id': id_})

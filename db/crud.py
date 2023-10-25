from abc import ABC

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


class __MongoCRUD(ABC):
    """
    абстрактный класс для работы с mongodb
    """

    @staticmethod
    def _create_document(collection: Collection, document: dict) -> str:
        """ Function to insert a document into a collection and
        return the document's id. """
        return str(collection.insert_one(document).inserted_id)

    @staticmethod
    def _get_document(collection: Collection, elements: dict, multiple: bool = False) -> list:
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements. """
        if multiple:
            results = collection.find(elements)
        else:
            results = collection.find_one(elements)
        return [r for r in results]

    @staticmethod
    def _update_document(collection: Collection, query_elements: dict, new_values: dict) -> None:
        """ Function to update a single document in a collection. """
        collection.update_one(query_elements, {'$set': new_values})

    @staticmethod
    def _delete_document(collection: Collection, query: dict) -> None:
        """ Function to delete a single document from a collection. """
        collection.delete_one(query)


class AgentCRUD(__MongoCRUD):
    __collection: Collection = agents

    @staticmethod
    def create(agent: Agent) -> str:
        """ Создание агента. Агент - представитьель и организатор события """
        return super()._create_document(
            AgentCRUD.__collection,
            agent.model_dump()
        )

    @staticmethod
    def get_by_title(title: str) -> list:
        """ Получеение данных о агенте """
        return super()._get_document(
            AgentCRUD.__collection,
            {"title": title}
        )


class EventCRUD(__MongoCRUD):
    __collection: Collection = events

    @staticmethod
    def create(event: Event) -> str:
        """ Создание события """
        return super()._create_document(
            EventCRUD.__collection,
            event.model_dump()
        )

    @staticmethod
    def get_by_title(title: str) -> list:
        """ Получеение данных о событии """
        return super()._get_document(
            EventCRUD.__collection,
            {"title": title},
            multiple=True
        )


class AppointmentCRUD(__MongoCRUD):
    __collection: Collection = appointments

    @staticmethod
    def make_an_appointment(appointment: Appointment, client_id: int) -> None:
        """ Запись клиента на событие  """
        super()._update_document(
            AppointmentCRUD.__collection,
            {"_id": appointment.id_},
            {"client_id": client_id}
        )

    @staticmethod
    def create(appointment: Appointment) -> str:
        """ Создание записи на событие """
        return super()._create_document(
            AppointmentCRUD.__collection,
            appointment.model_dump()
        )

    @staticmethod
    def get_by_client_id(client_id: int) -> list:
        """ Получеение данных о записи клиента """
        return super()._get_document(
            AppointmentCRUD.__collection,
            {'client_id': client_id}
        )


class ClientCRUD(__MongoCRUD):
    __collection: Collection = clients

    @staticmethod
    def create(client: Client) -> str:
        """ Создание клиента """
        return super()._create_document(
            ClientCRUD.__collection,
            client.model_dump()
        )

    @staticmethod
    def get_by_id(id_: int) -> list:
        """ Получеение данных о клиенте """
        return super()._get_document(
            ClientCRUD.__collection,
            {'_id': id_}
        )

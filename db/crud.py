from abc import ABC

from pymongo.collection import Collection
from pydantic import UUID4

from Collections import (
    agents,
    events,
    appointments,
    clients,
)

from models import (
    Event,
    Agent,
    Client,
    Appointment,
)


class _MongoCRUD(ABC):
    """
    абстрактный класс для работы с mongodb
    """

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


class AgentCRUD:
    __collection: Collection = agents

    @staticmethod
    def create(agent: Agent) -> str:
        """ Создание агента. Агент - представитьель и организатор события """

        return _MongoCRUD.create_document(
            AgentCRUD.__collection,
            agent.model_dump()
        )

    @staticmethod
    def get_by_title(title: str) -> list:
        """ Получеение данных о агенте """

        return _MongoCRUD.get_document(
            AgentCRUD.__collection,
            {"title": title}
        )


class EventCRUD:
    __collection: Collection = events

    @staticmethod
    def create(event: Event) -> str:
        """ Создание события """

        return _MongoCRUD.create_document(
            EventCRUD.__collection,
            event.model_dump()
        )

    @staticmethod
    def get_by_title(title: str) -> list[Event]:
        """ Получеение данных о событии """

        data = _MongoCRUD.get_document(
            EventCRUD.__collection,
            {"title": title},
            multiple=True
        )
        return [Event(**item) for item in data]


class AppointmentCRUD:
    __collection: Collection = appointments

    @staticmethod
    def make_an_appointment(appointment: Appointment, client_id: UUID4) -> None:
        """ Запись клиента на событие  """
        _MongoCRUD.update_document(
            AppointmentCRUD.__collection,
            {"_id": appointment.id},
            {"client_id": client_id}
        )

    @staticmethod
    def create(appointment: Appointment) -> str:
        """ Создание записи на событие """
        return _MongoCRUD.create_document(
            AppointmentCRUD.__collection,
            appointment.model_dump(by_alias=True)
        )

    @staticmethod
    def get_by_client_id(client_id: UUID4) -> list:
        """ Получеение данных о записи клиента """
        return _MongoCRUD.get_document(
            AppointmentCRUD.__collection,
            {'client_id': client_id}
        )

    @staticmethod
    def get_by_event_id(event_id: UUID4) -> list:
        """ Получеение данных о записи клиента """

        data = _MongoCRUD.get_document(
            AppointmentCRUD.__collection,
            {'event_id': event_id},
            multiple=True
        )

        return [Appointment(**item) for item in data]


class ClientCRUD:
    __collection: Collection = clients

    @staticmethod
    def create(client: Client) -> str:
        """ Создание клиента """
        return _MongoCRUD.create_document(
            ClientCRUD.__collection,
            client.model_dump()
        )

    @staticmethod
    def get(client_id: UUID4) -> Client:
        """ Получеение данных о клиенте """
        client_data = _MongoCRUD.get_document(
            ClientCRUD.__collection,
            {'_id': client_id}
        )[0]
        client = Client(**client_data)
        return client

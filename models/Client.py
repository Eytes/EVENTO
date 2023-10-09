from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    # second_name: str
    # phone_number: str


class ClientService:
    def get(self):
        '''получить клиента из БД'''
        pass

    def create(self):
        '''добавление клиента в БД'''
        pass

    def delete(self):
        '''удаление клиента из БД'''
        pass

    def update(self):
        '''изменить параметры / обновить данные клиента'''
        pass

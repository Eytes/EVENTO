from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    # description: str
    agent_id: int
    # date: str
    # type: str
    # status: str


class EventService:
    def get(self):
        '''получить событие из БД'''
        pass

    def create(self):
        '''добавление события в БД'''
        pass

    def delete(self):
        '''удаление события из БД'''
        pass

    def lock(self):
        '''заморозка возможности записи на событие'''
        pass

    def update(self):
        '''изменить параметры / обновить данные события'''
        pass

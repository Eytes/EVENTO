from pydantic import BaseModel


class Service(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    type: str
    lock: bool

    def get(self):
        '''получить услугу из БД'''
        pass

    def create(self):
        '''добавление услуги в БД'''
        pass

    def delete(self):
        '''удаление услуги из БД'''
        pass

    def lock(self):
        '''заморозка возможности записи на услугу'''
        pass

    def update(self):
        '''изменить параметры услуги / обновсить данные'''
        pass

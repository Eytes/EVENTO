from pydantic import BaseModel


class Service(BaseModel):
    id: int
    title: str
    data: str
    time: str
    owner_id: int

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
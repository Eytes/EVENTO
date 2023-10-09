from pydantic import BaseModel


class Agent(BaseModel):
    id: int
    title: str
    # rate: float


class AgentService:
    def get(self):
        """получить агента из БД"""
        pass

    def get_title(self):
        """ Получение названия агента """
        pass

    def create(self):
        """добавление агента в БД"""
        pass

    def delete(self):
        """удаление агента из БД"""
        pass

    def update(self):
        """изменить параметры / обновить данные агента"""
        pass

from pydantic import (
    BaseModel,
    Field,
)

from appointment.dto.Common import Message


class ClientBase(BaseModel):
    name: str
    # second_name: str
    # phone_number: str


class ClientId(BaseModel):
    id: int = Field(alias='_id')


class Client(ClientBase, ClientId):
    pass


class ErrorUserNotFound(BaseModel):
    message: Message = Message(
        ru='Пользователь не найден',
        en="User doesn't found"
    )


class RegisterErrorPhoneNumberExist(BaseModel):
    title_exist: bool
    message: Message = Message(
        ru='Клиент с таким номером уже зарегистрирован',
        en='Client with same phone number already registered'
    )

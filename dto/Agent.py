from pydantic import (
    BaseModel,
    Field,
)

from dto.Common import Message


# class AgentTitleUpdating(BaseModel):
#     new_title: str


class AgentBase(BaseModel):
    title: str
    # rate: float


class Agent(AgentBase):
    id: int = Field(alias='_id')


class ErrorAgentNotFound(BaseModel):
    message: Message = Message(
        ru='Агент не найден',
        en="Agent doesn't found"
    )


class RegisterErrorTitleExist(BaseModel):
    title_exist: bool
    message: Message = Message(
        ru='Агент с таким названием уже зарегистрирован',
        en='Agent with same title already registered'
    )

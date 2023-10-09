from pydantic import (
    BaseModel,
    Field,
)


class EventFullInfo(BaseModel):
    id: int
    title: str
    # description: str
    owner_id: int
    # type: str
    # lock: bool

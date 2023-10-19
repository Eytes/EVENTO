from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    # second_name: str
    # phone_number: str



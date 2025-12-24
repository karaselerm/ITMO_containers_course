from pydantic import BaseModel


class HelloResponse(BaseModel):
    message: str


class UserCreateRequest(BaseModel):
    name: str
    age: int


class UserCreateResponse(BaseModel):
    id: int
    name: str
    age: int

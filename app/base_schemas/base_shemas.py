from pydantic import BaseModel


class SBaseSchemaMenu(BaseModel):
    id: int
    name: str


class SBaseSchemaAddMenu(BaseModel):
    name: str


class SBaseSchemaSuccess(BaseModel):
    status: bool
    detail: str

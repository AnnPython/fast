from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UploadBook(BaseModel):
    bookname: str
    author: str
    year_publish: int
    amount_page: int


class GetListBook(BaseModel):
    id: int
    bookname: str
    author: str
    year_publish: int
    amount_page: int


class GetBook(GetListBook):
    user: User


class Message(BaseModel):
    message: str

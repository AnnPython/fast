#import aiofiles
from uuid import uuid4
from fastapi import HTTPException
from . import models, schemas

from book.schemas import UploadBook


async def save_book(
        user: models.User,
        bookname: str,
        author: str,
        year_publish: int,
        amount_page: int
):
    info = schemas.UploadBook(bookname=bookname, author=author, year_publish=year_publish, amount_page=amount_page, user=user.id)
    return await models.Book.objects.create(**info.dict())


async def update_book(
    id: int,
    bookname: str,
    author: str,
    year_publish: int,
    amount_page: int
):
    query_book = await models.Book.objects.get(id=id)
    if not query_book:
        raise HTTPException(status_code=404, detail="data not found")
    info = schemas.UploadBook(id=query_book.id, bookname=bookname, author=author, year_publish=year_publish, amount_page=amount_page)
    return await query_book.upsert(**info.dict())

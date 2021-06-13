from typing import List
from starlette.requests import Request
from fastapi import APIRouter, Form, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from user.auth import current_active_user
from . import models, schemas, services


book_router = APIRouter(tags=["book"])
templates = Jinja2Templates(directory="templates")


@book_router.post("/")
async def create_book(
        bookname: str = Form(...),
        author: str = Form(...),
        year_publish: int = Form(...),
        amount_page: int = Form(...),
        user: models.User = Depends(current_active_user)
):
    return await services.save_book(user, bookname, author, year_publish, amount_page)


@book_router.put("/update/{id}")
async def update_book(
        id: int,
        bookname: str = Form(...),
        author: str = Form(...),
        year_publish: int = Form(...),
        amount_page: int = Form(...),
):

    return await services.update_book(id, bookname, author, year_publish, amount_page)


@book_router.get("/user/{user_pk}", response_model=List[schemas.GetListBook])
async def get_list_book(user_pk: str):
    return await models.Book.objects.filter(user=user_pk).all()


@book_router.get("/books", response_model=List[schemas.GetListBook])
async def get_book_list(request: Request):
    return await models.Book.objects.all()


@book_router.get("/query-book/{book_name}", response_model=List[schemas.GetListBook])
async def get_name_book(book_name: str):
    return await models.Book.objects.filter(bookname=book_name).all()


@book_router.get("/query-pages/{maxpage}/{minpage}", response_model=List[schemas.GetListBook])
async def get_query_page(maxpage: int, minpage: int):
    return await models.Book.objects.filter(amount_page__gte=minpage, amount_page__lte=maxpage).all()


@book_router.get("/book", response_class=HTMLResponse)
async def get_book(request: Request):
    books = await models.Book.objects.select_related('user').all()
    return templates.TemplateResponse("listbook.html", {"request": request, "books": books})

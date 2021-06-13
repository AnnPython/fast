from typing import Optional, Union, Dict
import ormar

from database.db import MainMeta

from user.models import User


class Book(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    bookname: str = ormar.String(max_length=100, nullable=False)
    author: str = ormar.String(max_length=100, nullable=False)
    year_publish: int = ormar.Integer()
    amount_page: int = ormar.Integer()
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User)

    class Meta(MainMeta):
        pass

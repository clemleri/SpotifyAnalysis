# followers.py
from pydantic import BaseModel, HttpUrl, PositiveInt
from typing import Optional

class Followers(BaseModel):
    href: Optional[HttpUrl] = None
    total : PositiveInt
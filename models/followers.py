# followers.py
from pydantic import BaseModel
from typing import Optional, HttpUrl, conint, PositiveInt

class Followers(BaseModel):
    href: Optional[HttpUrl] = None
    total : PositiveInt
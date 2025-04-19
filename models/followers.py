from pydantic import BaseModel
from typing import Optional

class Followers(BaseModel):
    href: Optional[str] = None
    total : int
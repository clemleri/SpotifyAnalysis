from typing import List, Optional
from pydantic import BaseModel
from models.cursors import Cursors

class PaginatedResponse(BaseModel):
    href: str                 
    limit: int                
    next: Optional[str]   
    cursors : Optional[Cursors] = None
    offset: int               
    previous: Optional[str]   
    total: int               
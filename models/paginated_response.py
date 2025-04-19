from typing import List, Optional
from pydantic import BaseModel

class PaginatedResponse(BaseModel):
    href: str                 
    limit: int                
    next: Optional[str]       
    offset: int               
    previous: Optional[str]   
    total: int               
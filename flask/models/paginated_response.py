# paginated_response.py
from typing import Optional, List
from pydantic import BaseModel, conint, HttpUrl
from models.cursors import Cursors

class PaginatedResponse(BaseModel):
    href: HttpUrl                             # lien vers cette page de résultats
    limit: conint(ge=1, le=50)                       # nombre d'éléments demandés (>=1)
    next: Optional[HttpUrl] = None            # lien vers la page suivante
    cursors: Optional[Cursors] = None         # pointeurs pour pagination basée sur curseurs
    offset: conint(ge=0)                      # décalage de départ (>=0)
    previous: Optional[HttpUrl] = None        # lien vers la page précédente
    total: conint(ge=0)                       # nombre total d'éléments (>=0)
# simplified_album.py
from typing import List, Literal
import re
from pydantic import BaseModel, conlist, constr, conint, HttpUrl, root_validator
from models.external_urls import ExternalUrls
from models.image import Image
from models.simplified_artist import SimplifiedArtist

class SimplifiedAlbum(BaseModel):
    album_type: Literal['album', 'single', 'compilation', 'appears_on']
    artists: conlist(SimplifiedArtist, min_items=1)
    available_markets: conlist(
        constr(regex=r'^[A-Z]{2}$'),  # codes ISO 3166‑1 alpha‑2
        min_items=1
    )
    external_urls: ExternalUrls
    href: HttpUrl
    id: constr(regex=r'^[A-Za-z0-9]{22}$')  # Spotify IDs font 22 caractères
    images: conlist(Image, min_items=1)
    name: constr(min_length=1)
    release_date: constr(regex=r'^\d{4}(?:-\d{2}(?:-\d{2})?)?$')
    release_date_precision: Literal['year', 'month', 'day']
    total_tracks: conint(ge=1)
    type: Literal['album']
    uri: constr(regex=r'^spotify:album:[A-Za-z0-9]{22}$')

    @root_validator
    def check_release_date_matches_precision(cls, values):
        date = values.get('release_date')
        precision = values.get('release_date_precision')
        if precision == 'year' and not re.fullmatch(r'\d{4}', date):
            raise ValueError('Pour precision "year", release_date doit être au format YYYY')
        if precision == 'month' and not re.fullmatch(r'\d{4}-\d{2}', date):
            raise ValueError('Pour precision "month", release_date doit être au format YYYY-MM')
        if precision == 'day' and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
            raise ValueError('Pour precision "day", release_date doit être au format YYYY-MM-DD')
        return values

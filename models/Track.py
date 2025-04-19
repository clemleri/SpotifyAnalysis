from pydantic import BaseModel
from Album.py import Album
from Artist.py import Artist

class Track(BaseModel) :
    album : Album
    artists : Array(Artist)
    
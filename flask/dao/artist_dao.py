from config import db
from sqlalchemy.exc import IntegrityError
from models.sql_alchemy_models.sql_models.artist_sql_model import Artist
from models.sql_alchemy_models.metadata_sql_models.artist_metadata_model import ArtistMetadata
from typing import Optional, List
from datetime import datetime
from constants.tests import ARTIST_TYPE


class ArtistDAO:
    @staticmethod
    def add_artist(artist_data : ARTIST_TYPE) -> None:
        """
        Ajoute ou met à jour un artiste avec ses métadonnées.
        """
        artist = Artist(
            id=artist_data.id
        )
        metadata = ArtistMetadata(
            artist_id=artist_data.id,
            followers=artist_data.followers.total,
            popularity=artist_data.popularity,
            genres=artist_data.genres,
            image=artist_data.images[0].url,
            last_fetched=datetime.utcnow()
        )

        db.session.merge(artist)
        db.session.merge(metadata)
        db.session.commit()

    @staticmethod
    def get_artist_by_id(artist_id: str) -> Optional[Artist]:
        return Artist.query.get(artist_id)

    @staticmethod
    def get_artist_with_metadata(artist_id: str) -> Optional[dict]:
        artist = Artist.query.get(artist_id)
        if artist and artist.metadata:
            return {
                "id": artist.id,
                "followers": artist.metadata.followers,
                "popularity": artist.metadata.popularity,
                "genres": artist.metadata.genres,
                "image": artist.metadata.image,
                "last_fetched": artist.metadata.last_fetched.isoformat()
            }
        return None

    @staticmethod
    def search_artists_by_name(query: str) -> List[Artist]:
        # Nécessite un champ name dans Artist si on l'utilise ici
        return Artist.query.filter(Artist.name.ilike(f"%{query}%")).all()

    @staticmethod
    def delete_artist(artist_id: str) -> None:
        metadata = ArtistMetadata.query.get(artist_id)
        artist = Artist.query.get(artist_id)
        if metadata:
            db.session.delete(metadata)
        if artist:
            db.session.delete(artist)
        db.session.commit()

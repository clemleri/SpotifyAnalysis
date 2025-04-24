from flask.api_server import db
from datetime import datetime

class AlbumMetadata(db.Model):
    __tablename__ = 'album_metadata'
    album_id = db.Column(db.String(22), db.ForeignKey('albums.id'), primary_key=True)
    album_type = db.Column(db.String(22))
    album_name = db.Column(db.String(128))
    image = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    total_tracks = db.Column(db.Integer, nullable=False)
    last_fetched = db.Column(db.DateTime, default=datetime.utcnow)
    album = db.relationship('Album', back_populates='metadata')
from flask.api_server import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.String(22), primary_key=True)
    metadata = db.relationship('ArtistMetadata', uselist=False, back_populates='artist')
from flask.api_server import db


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.String(22), primary_key=True)
    tracks = db.relationship('Track', back_populates='album')
    metadata = db.relationship('AlbumMetadata', uselist=False, back_populates='album')
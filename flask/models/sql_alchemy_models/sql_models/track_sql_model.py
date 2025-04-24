from flask.api_server import db

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    duration_ms = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.String(22), db.ForeignKey('albums.id'), nullable=False)
    popularity = db.Column(db.Integer, nullable=True)
    metadata = db.relationship('TrackMetadata', uselist=False, back_populates='track')
    album = db.relationship("Album", back_populates="tracks")
    streams = db.relationship("TrackStream", back_populates="track")
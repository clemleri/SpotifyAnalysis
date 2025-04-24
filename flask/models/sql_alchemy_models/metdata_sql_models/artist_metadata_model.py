from flask.api_server import db

class ArtistMetadata(db.Model):
    __tablename__ = 'artist_metadata'
    artist_id = db.Column(db.String(22), db.ForeignKey('artists.id'), primary_key=True)
    followers = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    genres = db.Column(db.ARRAY(db.String))
    image = db.Column(db.String)
    last_fetched = db.Column(db.DateTime, default=datetime.utcnow)
    artist = db.relationship('Artist', back_populates='metadata')

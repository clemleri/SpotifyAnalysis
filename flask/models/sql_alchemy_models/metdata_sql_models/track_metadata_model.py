from flask.api_server import db

class TrackMetadata(db.Model):
    __tablename__ = 'track_metadata'
    track_id = db.Column(db.String(22), db.ForeignKey('tracks.id'), primary_key=True)
    popularity = db.Column(db.Integer)
    image = db.Column(db.String)
    last_fetched = db.Column(db.DateTime, default=datetime.utcnow)
    track = db.relationship('Track', back_populates='metadata')
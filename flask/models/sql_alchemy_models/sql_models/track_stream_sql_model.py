from flask.api_server import db

class TrackStream(db.Model):
    __tablename__ = 'track_plays'
    user_id = db.Column(db.String(22), db.ForeignKey('users.id'), primary_key=True)
    track_id = db.Column(db.String(22), db.ForeignKey('tracks.id'), primary_key=True)
    played_at = db.Column(db.DateTime, nullable=False)
    played_count = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", back_populates="streams")
    track = db.relationship("Track", back_populates="streams")
    __table_args__ = (
        db.Index('ix_user_played_at', 'user_id', 'played_at'),
    )
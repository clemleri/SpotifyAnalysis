from dao.db import db

class TrackStream(db.Model):
     __tablename__ = 'track_streams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(22), db.ForeignKey('users.id'), nullable=False)
    track_id = db.Column(db.String(22), nullable=False)  # Spotify ID du morceau
    played_at = db.Column(db.DateTime, nullable=False)
    play_count = db.Column(db.Integer, nullable=False, default=1)

    user = db.relationship('User', back_populates='stream_history')
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'track_id', 'played_at', name='uq_user_track_datetime'),
    )
    
    
from flask.api_server import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(22), primary_key=True)
    display_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    country = db.Column(db.String(2), nullable=False)
    product = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    streams = db.relationship("TrackStream", back_populates="user")
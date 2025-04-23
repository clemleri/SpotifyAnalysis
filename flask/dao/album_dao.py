from dao.db import db

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.String(10), nullable=True)
    
    tracks = db.relationship("Track", back_populates="album")
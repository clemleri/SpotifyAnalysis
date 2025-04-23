from dao.db import db

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
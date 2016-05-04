from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    score = db.Column(db.Integer)

    def __init__(self, name, score=2000):
        self.name = name
        self.score = score

    def __repr__(self):
        return '<id {}>'.format(self.id)
    

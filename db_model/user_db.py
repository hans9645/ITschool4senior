from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db= SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer(11), primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    user_name = db.Column(db.String(45), nullable=False)
    create_at = db.Column(db.DateTime)

    def __init__(self, user_id, password, user_name):
        self.user_id=user_id
        self.paswword=password
        self.user_name=user_name
        self.create_at=datetime.now()


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Members(db.Model):
    """ table name : user_info
        table info 
    - id : index id 회원생성 시 순서
    - user_id 
    - password
    - user_name
    - create_at : 생성 날짜 """
    
    __tablename__ = 'user_info'
    #문자들을 넣을 때 utf-8 형태로 들어가 한글을 인식할 수 있다.
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    user_name = db.Column(db.String(15), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, id, user_id, password, user_name, create_at):
        self.id = id
        self.user_id = user_id
        self.password = password
        self.user_name = user_name
        self.create_at = create_at

    #객체 자체로 print 찍었을 때 어떤 모습으로 보여줄지 정해주는것. 굳이 안해도 될듯?
    def __repr__(self):
        return 'id: %d, user_id : %s, password : %s, user_name : %s' % (self.id, self.user_id, self.password, self.user_name)

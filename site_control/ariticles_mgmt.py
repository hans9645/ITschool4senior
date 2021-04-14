from flask_login import UserMixin
from db_model.mysql import conn_mysqldb
from datetime import datetime
from sqlalchemy import create_engine, text


class Article():

    def __init__(self,user_id, title,context):
        self.user_id=user_id
        self.title=title,
        self.context=context
        
        
    
    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def get_board():
        mysql_db=conn_mysqldb()
        rows=mysql_db.execute("SELECT * FROM articles ORDER BY create_at DESC").fetchall() 
        return rows

    @staticmethod
    def write_post(user_id,title,context):
        mysql_db=conn_mysqldb()
        mysql_db.execute("INSERT INTO articles(user_id, title, context) VALUES ('%s','%s','%s')"%(str(user_id),str(title),str(context)))

    

    @staticmethod
    def delete(user_id):
        mysql_db=conn_mysqldb()
        db_cursor=mysql_db.cursor()
        deleted=mysql_db.execute("DELETE FROM user_info WHERE user_id= '%d' " %(user_id))
        return deleted



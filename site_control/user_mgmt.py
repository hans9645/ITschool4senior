from flask_login import UserMixin
from db_model.mysql import conn_mysqldb


class User(UserMixin):

    def __init__(self,user_id, password,user_name):
        self.id=user_id
        self.password=password
        self.name=user_name
        
    
    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db=conn_mysqldb()
        db_cursor=mysql_db.cursor()
        sql="SELECT * FROM user_info WHERE USER_ID='"+str(user_id)+"'"
        #print(sql) 터미널 등에서 코드상으로 확인후 작업하는게 좋다. 에러가 잘뜬단다.
        db_cursor.execute(sql)
        user=db_cursor.fetchone()
        if not user:
            return None
        user=User(user_id=user[0], password=user[1],user_name=user[2])
        return user


    @staticmethod
    def find(user_id):
        mysql_db=conn_mysqldb()
        db_cursor=mysql_db.cursor()
        sql="SELECT * FROM user_info WHERE USER_ID='"+str(user_id)+"'"
        #print(sql) 터미널 등에서 코드상으로 확인후 작업하는게 좋다. 에러가 잘뜬단다.
        db_cursor.execute(sql)
        user=db_cursor.fetchone() 
        if not user:
            return None
        user=User(user_id=user[0], password=user[1],user_name=user[2])
        return user



    @staticmethod
    def create(user_id, password,user_name):
        user=User.find(user_id)
        if user==None:
            mysql_db=conn_mysqldb()
            db_cursor=mysql_db.cursor()
            sql="INSERT INTO user_info (USER_ID, PASSWORD,USER_NAME) VALUES ('%s','%s','%s')"%(str(user_id),str(password),str(user_name))
            db_cursor.execute(sql)
            mysql_db.commit() #mysql에 데이터 변형이 일어나는 것이므로 커밋을 하는 게 좋다.
            return User.find(user_id)
        else:
            return user
            

    @staticmethod
    def delete(user_id):
        mysql_db=conn_mysqldb()
        db_cursor=mysql_db.cursor()
        sql="DELETE FROM user_info WHERE user_id= %d " %(user_id)
        deleted=db_cursor.execute(sql)
        mysql_db.commit() #mysql에 데이터 변형이 일어나는 것이므로 커밋을 하는 게 좋다.
        return deleted

import pymysql

MYSQL_HOST='localhost'
MYSQL_CONN=pymysql.connect(
    host= MYSQL_HOST ,
    port=3306 ,
    user='',
    passwd='' ,
    db='itschool4senior',
    charset='utf8'
)


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.close()
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
#데이터베이스와 연결이 끊길 경우 확인 후 다시 연결하거나 이미 연결되어 있는 경우에는 
#return 으로 연결된 객체를 반환하도록 함.


from sqlalchemy.pool import QueuePool
import mysql.connector
import os

# host=os.getenv('MYSQL_HOST', '127.0.0.1'),
# port=int(os.getenv('MYSQL_PORT', 3306)),
# user=os.getenv('MYSQL_USER', 'isucari'),
# password=os.getenv('MYSQL_PASS', 'isucari'),
# database=os.getenv('MYSQL_DBNAME', 'isucari'),


host = '127.0.0.1'
port = 3306
user = 'isucari'
password = 'isucari'
database = 'isucari'

cnxpool = QueuePool(lambda: mysql.connector.connect(host=host, user=user, password=password, database=database), pool_size=200)

def get_connection():
    return cnxpool.connect()

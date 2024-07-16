import mysql.connector
from mysql.connector import Error

host_name = "127.0.0.1"
user_name = "root"
user_password = "public"
db_name = "temp_data"

def get_db_connection():
    """获取数据库连接"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def get_latest_temperature(connection):
    """获取最新的温度数据（假设数据库中有相应的表和列）"""
    cursor = connection.cursor()
    # 假设您有一个名为 temp_data 的表，并且您想要获取最新的一条记录
    cursor.execute("SELECT timestamp, temperature FROM temp_data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        return {'timestamp': row[0], 'temperature': row[1]}
    return None


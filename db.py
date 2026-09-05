from pymysql import connect

def get_connection():
    connection=connect(
        host="localhost",
        user="root",
        password="Gopi@bindu",
        database="agriculture"
    )
    return connection
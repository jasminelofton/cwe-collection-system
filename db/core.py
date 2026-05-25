import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def drop_table(t_name, cursor, connection):
    sql_command = f"DROP TABLE IF EXISTS {t_name}"
    cursor.execute(sql_command)
    connection.commit()

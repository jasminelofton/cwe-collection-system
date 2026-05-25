def create_related_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF NOT EXISTS Relateds
        (
        related_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        related TEXT NOT NULL
        );
        """
    cursor.execute(sql_command)
    connection.commit()

def select_records_related_table(cursor):
    cursor.execute("SELECT * FROM Relateds")
    return cursor.fetchall()

def insert_related(related, cursor, connection):
    sql_command = "INSERT INTO Relateds (related) VALUES (?)"
    cursor.execute(sql_command, (related,))
    connection.commit()

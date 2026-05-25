def create_impacts_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF NOT EXISTS Impacts
        (
        impact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        impact TEXT NOT NULL
        );
        """
    cursor.execute(sql_command)
    connection.commit()

def select_records_impacts_table(cursor):
    cursor.execute("SELECT * FROM Impacts")
    return cursor.fetchall()

def insert_impact(impact, cursor, connection):
    sql_command = "INSERT INTO Impacts (impact) VALUES (?)"
    cursor.execute(sql_command, (impact,))
    connection.commit()

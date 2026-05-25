def create_weakness_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF NOT EXISTS Weaknesses
        (
        Cwe_id INTEGER PRIMARY KEY NOT NULL,
        Title TEXT NOT NULL,
        Description TEXT
        )
        """
    cursor.execute(sql_command)
    connection.commit()

def insert_record_in_weakness_table(cwe_id, title, description, cursor, connection):
    sql_command = """
        INSERT INTO Weaknesses(Cwe_id, Title, Description) VALUES(?, ?, ?)
        """
    cursor.execute(sql_command, (cwe_id, title, description))
    connection.commit()

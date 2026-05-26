def create_relateds_to_weaknesses_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF NOT EXISTS Relateds_To_Weaknesses
        (
        weakness_id INTEGER NOT NULL,
        related_id INTEGER NOT NULL,
        PRIMARY KEY (weakness_id, related_id),
        FOREIGN KEY (weakness_id) REFERENCES Weaknesses(Cwe_id),
        FOREIGN KEY (related_id) REFERENCES Relateds(related_id)
        );
        """
    cursor.execute(sql_command)
    connection.commit()

def insert_related_to_weakness(weakness_id, related_id, cursor, connection):
    sql_command = """
        INSERT INTO Relateds_To_Weaknesses (weakness_id, related_id) VALUES (?, ?)
        """
    cursor.execute(sql_command, (weakness_id, related_id))
    connection.commit()

def select_relateds_for_weakness(weakness_id, cursor):
    sql_command = """
        SELECT r.related_id, r.related
        FROM Relateds r
        JOIN Relateds_To_Weaknesses rtw ON r.related_id = rtw.related_id
        WHERE rtw.weakness_id = ?
        """
    cursor.execute(sql_command, (weakness_id,))
    return cursor.fetchall()

def select_weaknesses_for_related(related_id, cursor):
    sql_command = """
        SELECT w.Cwe_id, w.Title, w.Description
        FROM Weaknesses w
        JOIN Relateds_To_Weaknesses rtw ON w.Cwe_id = rtw.weakness_id
        WHERE rtw.related_id = ?
        """
    cursor.execute(sql_command, (related_id,))
    return cursor.fetchall()

def select_all_records_relateds_to_weaknesses(cursor):
    sql_command = """
        SELECT * FROM Relateds_To_Weaknesses
        """
    cursor.execute(sql_command)
    return cursor.fetchall()
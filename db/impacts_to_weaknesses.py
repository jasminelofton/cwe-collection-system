def create_impacts_to_weaknesses_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF NOT EXISTS Impacts_To_Weaknesses
        (
        weakness_id INTEGER NOT NULL,
        impact_id INTEGER NOT NULL,
        PRIMARY KEY (weakness_id, impact_id),
        FOREIGN KEY (weakness_id) REFERENCES Weaknesses(Cwe_id),
        FOREIGN KEY (impact_id) REFERENCES Impacts(impact_id)
        );
        """
    cursor.execute(sql_command)
    connection.commit()

def insert_impact_to_weakness(weakness_id, impact_id, cursor, connection):
    sql_command = """
        INSERT INTO Impacts_To_Weaknesses (weakness_id, impact_id) VALUES (?, ?)
        """
    cursor.execute(sql_command, (weakness_id, impact_id))
    connection.commit()

def select_impacts_for_weakness(weakness_id, cursor):
    sql_command = """
        SELECT i.impact_id, i.impact
        FROM Impacts i
        JOIN Impacts_To_Weaknesses itw ON i.impact_id = itw.impact_id
        WHERE itw.weakness_id = ?
        """
    cursor.execute(sql_command, (weakness_id,))
    return cursor.fetchall()

def select_weaknesses_for_impact(impact_id, cursor):
    sql_command = """
        SELECT w.Cwe_id, w.Title, w.Description
        FROM Weaknesses w
        JOIN Impacts_To_Weaknesses itw ON w.Cwe_id = itw.weakness_id
        WHERE itw.impact_id = ?
        """
    cursor.execute(sql_command, (impact_id,))
    return cursor.fetchall()

def select_all_records_impacts_to_weaknesses(cursor):
    sql_command = """
        SELECT * FROM Impacts_To_Weaknesses
        """
    cursor.execute(sql_command)
    return cursor.fetchall()
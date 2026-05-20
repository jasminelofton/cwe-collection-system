import sqlite3

# create a database if it does not exist
def create_database(db_name):
    connection = sqlite3.connect(name)
    return connection

# drop a table from a database by table name
def drop_table(t_name, cursor, connection):
    sql_command = f"DROP TABLE IF EXISTS {t_name}"
    cursor.execute(sql_command) 
    connection.commit()

# The table to hold basic information of each ALLOWED CWE 
def create_weakness_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF EXISTS Weaknesses
        (
        Cwe_id INTEGER PRIMARY KEY NOT NULL,
        Title TEXT NOT NULL,
        Description TEXT
        )
        """
    cursor.execute(sql_command)
    connection.commit()

# The table to connect CWE_ids to one or more security impacts
def create_impacts_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF EXISTS Impacts
        (
        Cwe_id INTEGER NOT NULL,
        Impact TEXT NOT NULL,
        FOREIGN KEY (Cwe_id) REFERENCES Weaknesses(Cwe_id)
        );
        """
    cursor.execute(sql_command)
    connection.commit()

# The table to connect CWE_ids to one or more related security designs
def create_related_table(cursor, connection):
    sql_command = """
        CREATE TABLE IF EXISTS Relateds
        (
        Cwe_id INTEGER NOT NULL,
        Related TEXT NOT NULL,
        FOREIGN KEY (Cwe_id) REFERENCES Weaknesses(Cwe_id)
        );
        """
    cursor.execute(sql_command)
    connection.commit()


def insert_record_in_weakness_table(cwe_id, title, description, cursor, connection):
    sql_command = """
        INSERT INTO weakness(Cwe_id, Title, Description) VALUES(?, ?, ?)
        """
    cursor.execute(sql_command, (cwe_id, title, description))
    connection.commit()



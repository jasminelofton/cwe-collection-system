import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import *

CSV_PATH = os.path.join(os.path.dirname(__file__), "More Weaknesses(CWEs Analyzed) - Updated copy.csv")

connection = create_database("cwe.db")
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

drop_table("Impacts_To_Weaknesses", cursor, connection)
drop_table("Relateds_To_Weaknesses", cursor, connection)
drop_table("Weaknesses", cursor, connection)

create_weakness_table(cursor, connection)
create_impacts_to_weaknesses_table(cursor, connection)
create_relateds_to_weaknesses_table(cursor, connection)

# build lookup maps from already-populated Impacts and Relateds tables
impact_lookup = {impact: impact_id for impact_id, impact in select_records_impacts_table(cursor)}
related_lookup = {related: related_id for related_id, related in select_records_related_table(cursor)}

def parse_phrases(raw):
    return {phrase.strip().lower().rstrip('.') for phrase in raw.replace('\xa0', ' ').split(',') if phrase.strip()}

with open(CSV_PATH, encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row['ID'].strip():
            continue
        cwe_id = int(row['ID'])
        name = row['Name'].strip()
        description = row['Description'].strip()

        insert_record_in_weakness_table(cwe_id, name, description, cursor, connection)

        for phrase in parse_phrases(row['Security Impact']):
            insert_impact_to_weakness(cwe_id, impact_lookup[phrase], cursor, connection)

        for phrase in parse_phrases(row['Security Related Design']):
            insert_related_to_weakness(cwe_id, related_lookup[phrase], cursor, connection)

        print(f"Inserted CWE-{cwe_id}: {name}")

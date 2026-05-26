#note: already added 'separation of privileges' so if you restart the table, this needs to be added manually

import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import *

CSV_PATH = os.path.join(os.path.dirname(__file__), "More Weaknesses(CWEs Analyzed) - Updated copy.csv")

relateds_set = set()

with open(CSV_PATH, encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row['Security Related Design'].replace('\xa0', ' ')
        for phrase in raw.split(','):
            normalized = phrase.strip().lower().rstrip('.')
            if normalized:
                relateds_set.add(normalized)


connection = create_database("cwe.db")

cursor = connection.cursor()

drop_table("Relateds", cursor, connection)

create_related_table(cursor, connection)

for related in relateds_set:
    insert_related(related, cursor, connection)

records = select_records_related_table(cursor)

for related_id, related in records:
    print(related_id, related)

import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import *

CSV_PATH = os.path.join(os.path.dirname(__file__), "More Weaknesses(CWEs Analyzed) - Updated copy.csv")

impacts_set = set()

with open(CSV_PATH, encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row['Security Impact'].replace('\xa0', ' ')
        for phrase in raw.split(','):
            normalized = phrase.strip().lower().rstrip('.')
            if normalized:
                impacts_set.add(normalized)

connection = create_database("cwe.db")
cursor = connection.cursor()

drop_table("Impacts", cursor, connection)
create_impacts_table(cursor, connection)

for impact in impacts_set:
    insert_impact(impact, cursor, connection)

records = select_records_impacts_table(cursor)

for impact_id, impact in records:
    print(impact_id, impact)

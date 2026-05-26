# Imports: database functions, scraper functions, HTTP request library, HTML parser
from db import *

from scraper import *

import requests

from bs4 import BeautifulSoup

# Name of the SQLite database file
db_name = "cwe.db"

# Total number of CWEs on the MITRE website
total_cwes = 1387

# Open a connection to the database and enable foreign key enforcement
connection = create_database(db_name)

connection.execute("PRAGMA foreign_keys = 1")

cursor = connection.cursor()

# Iterate over every CWE id from 1 to total_cwes
for i in range(1, total_cwes):
    print()
    # Skip this CWE if it has already been inserted into the Weaknesses table
    if (count_id_records_in_weaknesses_table(i, cursor) == 1):
        print(f'{i} already in database')
        continue

    # Build the URL for this CWE and fetch the page
    url = f"https://cwe.mitre.org/data/definitions/{i}.html"

    page = requests.get(url)

    # Parse the HTML so we can extract data from it
    soup = BeautifulSoup(page.text, 'html.parser')

    # Returns True if the CWE mapping is ALLOWED, False if PROHIBITED or RESTRICTED
    is_allowed_cwe = get_vulnerability_mapping(soup)

    # Only process CWEs whose mapping is ALLOWED
    if (is_allowed_cwe == False):
        print('is not allowed')
        continue

    # Extract the CWE title and description from the page
    title = get_title_string(soup)
    desc = get_description_string(soup)
    print(f'inserting cwe_{i} into database')
    #insert_record_in_weakness_table(i, title, desc, cursor, connection)

    # Scrape all impact-related text from the page
    impacts = retrieve_all_impacts(soup)

    # Load every known impact phrase from the Impacts table
    rows = select_records_impacts_table(cursor)

    phrases = [row[1] for row in rows]

    # Find which known impact phrases appear in the scraped impact text
    matches = []
    for sentence in impacts:
        for phrase in phrases:
            if phrase.lower() in sentence.lower():
                matches.append(phrase)
    print('printing the security impacts')
    print(set(matches))


    # Scrape all related-design text from the Potential Mitigations, Relationships, and Detection Methods sections
    related = retrieve_all_related(soup)

    # Load every known impact phrase from the Impacts table
    rows = select_records_related_table(cursor)

    phrases = [row[1] for row in rows]

    # Find which known impact phrases appear in the scraped impact text
    matches = []
    for sentence in related:
        for phrase in phrases:
            if phrase.lower() in sentence.lower():
                matches.append(phrase)
    print('printing the related security design')
    print(set(matches))
    print()

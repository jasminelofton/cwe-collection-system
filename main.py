from db import *

from scraper import *

import requests

from bs4 import BeautifulSoup

db_name = "cwe.db"

def add_remaining_CWEs():
    
    #connection = create_database()

    #connection.execute("PRGRMA foreign_keys = 1")

    #cursor = connection.cursor()

    #create_weakness_table()

    total_cwes = 1387

    #!Tester
    # tests Allowed works cleanely and it does print all functionality correctly
    # for i in range(1, 1387):
    #     url = f"https://cwe.mitre.org/data/definitions/{i}.html"

    #     page = requests.get(url)

    #     soup = BeautifulSoup(page.text, 'html.parser')

    #     mapping = get_vulnerability_mapping(soup)

    #     if (mapping != "ALLOWED"):
    #         print("NOPE: " + mapping)
    #         continue

    #     print(mapping)


    # !TESTER confirm title and desc id
    # for i in range(1, 1387):
    #     url = f"https://cwe.mitre.org/data/definitions/{i}.html"

    #     page = requests.get(url)

    #     soup = BeautifulSoup(page.text, 'html.parser')

    #     mapping = get_vulnerability_mapping(soup)

    #     if (mapping != "ALLOWED"):
    #         print("NOPE: " + mapping)
    #         continue

    #     print(mapping)
    #     title = get_title_string(soup)
    #     desc = get_description_string(soup)
    #     print(i)
    #     print(title)
    #     print(desc)



    # get all titles, descriptions, and ids
    for i in range(1, 1387):
        url = f"https://cwe.mitre.org/data/definitions/{i}.html"

        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        mapping = get_vulnerability_mapping(soup)

        if (mapping != "ALLOWED"):
            print("NOPE: " + mapping)
            continue

        print(mapping)
        title = get_title_string(soup)
        desc = get_description_string(soup)
        print(i)
        print(title)
        print(desc)


connection = create_database(db_name)

# connection.execute("PRAGMA foreign_keys = 1")

cursor = connection.cursor()

# url = "https://cwe.mitre.org/data/definitions/90.html"

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# retrieve_all_related(soup)

# sentences = retrieve_all_impacts(soup)

# rows = select_records_impacts_table(cursor)

# phrases = [row[1] for row in rows]

# matches = []
# for sentence in sentences:
#     for phrase in phrases:
#         if phrase.lower() in sentence.lower():
#             matches.append(phrase)

# print(set(matches))

# sentences = retrieve_all_related(soup)

# rows = select_records_related_table(cursor)

# phrases = [row[1] for row in rows]

# matches = []
# for sentence in sentences:
#     for phrase in phrases:
#         if phrase.lower() in sentence.lower():
#             matches.append(phrase)

# print(set(matches))


records = select_all_records_relateds_to_weaknesses(cursor)

for record in records:
    print(record)
from databasefunc import *

from parser import *

import requests

from bs4 import BeautifulSoup


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

add_remaining_CWEs()


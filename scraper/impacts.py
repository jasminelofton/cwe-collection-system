#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests



def retrieve_all_impacts(soup):
    all_impacts = []

    common_consequences = soup.select_one('#Common_Consequences table')
    
    all_impacts.extend(get_all_subheadings(common_consequences))

    all_impacts.extend(get_all_subotheading(common_consequences))

    all_impacts.extend(get_all_subotheading_blurb(common_consequences))

    return all_impacts
    

def get_all_subheadings(common_consequences):
    impacts = []

    rows = common_consequences.find_all('span', class_='subheading')

    for row in rows:
       impacts.append(row.get_text())

    return impacts

def get_all_subotheading(common_consequences):
    subotheading = []

    rows = common_consequences.find_all('span', class_='suboptheading')

    for row in rows:
       subotheading.append(row.get_text().split('Scope: ')[1])

    return subotheading

def get_all_subotheading_blurb(common_consequences):
    subotheading = []

    rows = common_consequences.find_all('div')

    for row in rows:
       subotheading.append(row.get_text())

    return subotheading    

#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests



def retrieve_all_related(soup):
    all_impacts = []

    common_consequences = soup.select_one('#Potential_Mitigations #Grouped table')

    all_impacts.extend(get_all_subheadings(common_consequences))

    all_impacts.extend(get_all_subotheading(common_consequences))

    all_impacts.extend(get_all_subotheading_blurb(common_consequences))

    relationships = soup.select_one('#Relationships')

    all_impacts.extend(get_all_relevant_tables(relationships))

    methods = soup.select_one('#Detection_Methods')

    all_impacts.extend(get_all_detection_methods(methods))

    return all_impacts
    

def get_all_subheadings(common_consequences):
    impacts = []

    rows = common_consequences.find_all('p', class_='subheading')

    for row in rows:
       impacts.append(row.get_text())

    return impacts

def get_all_subotheading(common_consequences):
    subotheading = []

    rows = common_consequences.find_all('p', class_='suboptheading')

    for row in rows:
        italics = row.find_all('i')
        for i in italics:
            subotheading.append(i.get_text())

    return subotheading


# a finicky implementation to retrieve the blurbs
def get_all_subotheading_blurb(common_consequences):
    subotheading = []

    rows = common_consequences.find_all('tr')[1:]  # skip header row
    for row in rows:
        tds = row.find_all('td')
        divs = tds[1].find_all('div')
        if len(divs) > 1:
            text = divs[1].get_text().strip().replace('\n', ' ')
            subotheading.append(text)
        else:
            text = divs[0].get_text().strip().replace('\n', ' ')
            subotheading.append(text)

    return subotheading    


# a finicky implementation to retrieve the blurbs
def get_all_relevant_tables(relationships):
    subotheading = []

    table_boxes = relationships.find_all(id='relevant_table')

    for table_box in table_boxes:

        relevant_tables = table_box.find('table').find_all(recursive=False)[1:]

        for table in relevant_tables:

            array = table.find_all('td', valign='top')

            for i in range(3, len(array), 4):   

                subotheading.append(array[i].get_text().strip())

    return subotheading    


def get_all_detection_methods(methods):
    subheading = []

    large_table = methods.find('div', class_='tabledetail').find('div', id='EntryStripedTable').select_one('table').find_all('p', class_= 'subheading')

    for item in large_table:
        subheading.append(item.get_text())

    return subheading
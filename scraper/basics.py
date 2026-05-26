#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests


# retrieve the title of a cwe through the beautiful soup html parser
# ret: title name.
def get_title_string(soup):
    title = soup.find('h2').get_text(strip = True)
    title_substring = title.split(": ", 1)[1]
    return title_substring


# retrieve the description text through the beautiful soup parser object.
# ret: a sentence.
def get_description_string(soup):
    return soup.find(id = 'Description').find(class_='indent').get_text(strip=True)

# retrieve the mapping of the cwe through the beautiful soup parser object.
# ret: True if ALLOWED, False otherwise (PROHIBITED or RESTRICTED).
def get_vulnerability_mapping(soup):
    mapping = soup.select_one('body table span.tool span').get_text(strip=True)
    return mapping == "ALLOWED"


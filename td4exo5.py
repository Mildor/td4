import requests
import lxml
from bs4 import BeautifulSoup


def get_definition(x):
    """ Get word definition from online dictionnary"""
    url = 'https://www.le-dictionnaire.com/definition/{0}'.format(x)
    ref = requests.get(url)
    html = BeautifulSoup(ref.text, 'lxml')
    divdefinition = html.find('div', class_='defbox')
    defi = divdefinition.findChildren('ul')
    defli = defi[0].findChildren('li')

    return defli[0].text


definition = {}
with open('vocabulary.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        definition[lines[i]] = get_definition(lines[i])

with open('definition.txt', 'w') as d:
    for k, v in definition.items():
        d.write(v + "\n")

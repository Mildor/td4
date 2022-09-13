import requests
from bs4 import BeautifulSoup
import pandas


UNI = requests.get("https://stackoverflow.com/questions/tagged/beautifulsoup")

quest = BeautifulSoup(UNI.text, 'lxml')
res = quest.find_all('h3', class_='s-post-summary--content-title')
votes = quest.find_all('div', class_='s-post-summary--stats-item s-post-summary--stats-item__emphasized')
answers = quest.find_all('div', class_='s-post-summary--stats-item has-answers')
childrenQ = []
childrenV = []
childrenA = []

for i in range(10):
    question = res[i].findChildren("a", recursive=False)
    vote = votes[i].findChildren('span', class_='s-post-summary--stats-item-number')
    answer = answers[i].findChildren('span', class_='s-post-summary--stats-item-number')
    childrenQ.append(question[0].getText())
    childrenV.append(vote[0].getText())
    childrenA.append(answer[0].getText())

data = {
    "titre": childrenQ,
    "votes": childrenV,
    "answers": childrenA
}
df = pandas.DataFrame(data, columns=["titre", "votes", "answers"])

df.to_csv("data.csv", index=0)

# Â ex4
def get_pagination(payload_def):
    r = requests.get('http://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html#nav',
                     params=payload_def)
    soup = BeautifulSoup(r.text, "lxml")
    pagemaxinput = soup.find('input', title='Aller à la dernière page')
    if pagemaxinput != None:
        lastPage = pagemaxinput.get('name')
        findchar = lastPage.find("-")
        pagination = lastPage[findchar+1:]
        return pagination
    else:
        return 1


def get_all_pages(payload_dynamic, pagination_def):
    i = 1
    while i <= int(pagination_def):
        payload_dyn = {
            "submit-form": payload_dynamic['submit-form'],
            "zone-item-id": payload_dynamic['zone-item-id'],
            "catalog": payload_dynamic['catalog'],
            "title": payload_dynamic['title'],
            "textfield": payload_dynamic['textfield'],
            "degree": payload_dynamic['degree'],
            "orgUnit": payload_dynamic['orgUnit'],
            "place": payload_dynamic['place'],
            "page-" + str(i): str(i)
        }
        req = requests.get('http://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html#nav',
                           params=payload_dyn)
        html = BeautifulSoup(req.text, "lxml")
        titli = html.find("ul", class_="custom")
        tit = titli.find_all('strong')
        for titre in tit:
            print(titre.text)
        i += 1


payload_lp = {
    "submit-form": "",
    "zone-item-id": "zoneItem://c8e50408-29b9-4eb9-9b3f-1c209fb2d75b",
    "catalog": "odf-2018-2022",
    "title": "",
    "textfield": "",
    "degree": "DP",
    "orgUnit": "",
    "place": ""
}

# pagination_lp = get_pagination(payload_lp)
# get_all_pages(payload_lp, pagination_lp)

payload_master = {
    "submit-form": "",
    "zone-item-id": "zoneItem://c8e50408-29b9-4eb9-9b3f-1c209fb2d75b",
    "catalog": "odf-2018-2022",
    "title": "",
    "textfield": "Ecologie",
    "degree": "XB",
    "orgUnit": "",
    "place": ""
}
# pagination_master = get_pagination(payload_master)
# get_all_pages(payload_master, pagination_master)

payload_orleans = {
    "submit-form": "",
    "zone-item-id": "zoneItem://c8e50408-29b9-4eb9-9b3f-1c209fb2d75b",
    "catalog": "odf-2018-2022",
    "title": "",
    "textfield": "",
    "degree": "",
    "orgUnit": "",
    "place": "45000"
}

pagination_orleans = get_pagination(payload_orleans)
get_all_pages(payload_orleans, pagination_orleans)


def get_definition(x):
    """ Get word definition from online dictionnary"""
    url = 'https://www.le-dictionnaire.com/definition/{0}'.format(x)
    ref = requests.get(url)
    html = BeautifulSoup(ref.text, 'lxml')
    divdefinition = html.find('div', class_='defbox')
    defi = divdefinition.findChildren('ul')
    defli = defi[0].findChildren('li')

    return defli[0].text


lines = []
definition = {}
with open('vocabulary.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        definition[lines[i]] = get_definition(lines[i])

with open('definition.txt', 'w') as d:
    for k, v in definition.items():
        d.write(v + "\n")


def recherche_marmiton(x):
    x = x.replace(' ', '-')
    j = []
    url = 'https://www.marmiton.org/recettes/recherche.aspx?aqt={0}&ttlt=30'.format(x)
    ref = requests.get(url)
    html = BeautifulSoup(ref.text, 'lxml')
    h = html.find_all('h4')
    for i in h:
        j.append(i.text)
    return j


rech = recherche_marmiton('noix de saint jacques')

print(rech)

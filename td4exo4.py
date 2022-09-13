import requests
import lxml
from bs4 import BeautifulSoup


def get_pagination(payload_def):
    r = requests.get('http://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html#nav',
                     params=payload_def)
    soup = BeautifulSoup(r.text, "lxml")
    pagemaxinput = soup.find('input', title='Aller à la dernière page')
    if pagemaxinput is not None:
        lastPage = pagemaxinput.get('name')
        findchar = lastPage.find("-")
        pagination = lastPage[findchar + 1:]
        return pagination
    else:
        return 1


def get_all_pages(payload_dynamic):
    i = 1
    titres = []
    pagination_def = get_pagination(payload_dynamic)
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
            titres.append(titre.text)
        i += 1
    return titres


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
lp = get_all_pages(payload_lp)
print(lp)

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
master = get_all_pages(payload_master)
print(master)

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
orleans = get_all_pages(payload_orleans)
print(orleans)

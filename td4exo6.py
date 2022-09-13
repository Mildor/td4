import requests
from bs4 import BeautifulSoup
import lxml
import json


def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}


def recherche_marmiton(payload):
    print(f"Votre recherche pour {payload['aqt']} a débuté veuillez patienté ...")
    dic = dict()
    recette = dict()
    invalid = [
        "name", "@context", "@type", "image", "thumbnailUrl", "video", "author", "keywords", "aggregateRating",
        "recipeCuisine", "description", "datePublished"
    ]
    pagination_mami = get_pagination_marmiton(payload)
    for index in range(int(pagination_mami)):
        payload_mamiton = {
            "aqt": payload['aqt'],
            "page": index+1
        }
        ref = requests.get('https://www.marmiton.org/recettes/recherche.aspx?', params=payload_mamiton)
        html = BeautifulSoup(ref.text, 'lxml')
        divrec = html.find('div', class_='MRTN__sc-1gofnyi-0 YLcEb')
        arec = divrec.findChildren('a')
        j = 0
        for valeurs in arec:
            lienrec = valeurs.get('href')
            if lienrec[0] != '/':
                url_rec=str(lienrec)
            else:
                url_rec='https://www.marmiton.org' + str(lienrec)
            req = requests.get(url_rec)
            if req.status_code == 200:
                soup_rec = BeautifulSoup(req.text, 'lxml')
                json_ld = soup_rec.find("script", {"type": "application/ld+json"}).text
                dic[j] = json.loads(json_ld)
                j += 1
            for k, v in dic.items():
                if '@type' in v and v['@type'] == 'Recipe':
                    totaltime = v['totalTime'][:-1]
                    totaltime = int(totaltime[2:])
                    if v['recipeYield'] == '2 personnes' and totaltime < 30:
                        recette[v['name']] = without_keys(v, invalid)
    print(f"Votre recherche pour {payload['aqt']} s'est finis sans érreurs")
    return recette


def get_pagination_marmiton(payload_marmit):
    r = requests.get('https://www.marmiton.org/recettes/recherche.aspx?', params=payload_marmit)
    soup = BeautifulSoup(r.text, "lxml")
    divpagination = soup.find_all('div', class_='SHRD__sc-dvq2vt-1')
    apagination = divpagination[-1].findChildren('a')
    if apagination is not None:
        lasta = apagination[-1]
        lastdiv = lasta.findChildren('div')
        pagination = lastdiv[-1].text
        return pagination
    else:
        apagination = divpagination[0].findChildren('a')
        lasta = apagination[-1]
        lastdiv = lasta.findChildren('div')
        pagination = lastdiv[-1].text
        return pagination


payload_marmiton = {
    "aqt": "coquilles saint jacques",
}

recettes = recherche_marmiton(payload_marmiton)
print(recettes)

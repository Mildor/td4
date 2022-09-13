import requests
from bs4 import BeautifulSoup
import lxml
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
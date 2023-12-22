import requests
from bs4 import BeautifulSoup

url = 'https://www.adorocinema.com/filmes/melhores/'

response = requests.get(url)


if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    tratedItens = []
    itens = soup.find_all('div', class_ = 'card entity-card entity-card-list cf')

    for item in itens:
        name = item.findChildren('h2', class_ = 'meta-title')
        namet = name[0].text
        director = item.findChildren('a', class_ = 'blue-link')
        directort = ""

        if len(director) > 0:
            directort = director[0].text
        else:
            director = item.findChildren('span', class_ = 'blue-link')
            directort = director[0].text

        lg = item.findChildren('div', class_ = 'meta-body-item meta-body-info')
        listGender = lg[0].findChildren('span')
        listGendert = []
        for i in listGender:
            if not (i.text == '/'):
                listGendert.append(i.text)
        itemt = {"nome": namet, "diretor": directort, "genero": listGendert}
        tratedItens.append(itemt)

else:
    print("Falha, status: {}".format(response.status_code))

for item in tratedItens:
    print(item)
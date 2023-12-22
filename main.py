import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'

response = requests.get(url)


if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # links = soup.find_all('a')
    # for link in links:
    #     print(link.get('href'))

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    for i in range(len(quotes)):
        print(authors[i].text, ":", quotes[i].text)


else:
    print("Falha, status: {}".format(response.status_code))
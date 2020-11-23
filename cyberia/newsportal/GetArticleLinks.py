from bs4 import BeautifulSoup
import requests

articletitles = []
articlelinks = []
articlesdict = {}

def getCSOlinks(url):
    urlRequest = requests.get(url)

    soup = BeautifulSoup(urlRequest.content, 'html.parser')
    articles = soup.find_all(class_='river-well article')

    for article in articles:
        title = article.find('h3')
        articletitles.append(title.text)
        link = article.find('a')['href']
        articlelinks.append(link)
        articlesdict[title.text] = link
    return articlesdict


#getCSOlinks('https://www.csoonline.com/news/')

#print(articletitles[0])
#print(articlelinks[0])


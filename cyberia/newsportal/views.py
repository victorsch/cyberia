from django.shortcuts import render
from .GetArticleLinks import getCSOlinks


# Create your views here.
def index(request):
    return render(request, 'index.html')

def newsportal(request):
    csodict = getCSOlinks('https://www.csoonline.com/news/')
    top10CSO = []
    top10CSOLinks = []
    for article in csodict:
        #print(article, end="\n\n")
        top10CSO.append(article)
        top10CSOLinks.append(csodict[article])
    sentDictionary = {}
    sentDictionary['top10CSO'] = top10CSO[:10]
    sentDictionary['top10CSOLinks'] = top10CSO[:10]
    sentDictionary['csodict'] = csodict
    return render(request, 'newsportal.html', sentDictionary)



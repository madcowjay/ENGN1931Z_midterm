import feedparser
import re
# from bs4 import BeautifulSoup

def special_repl(matchobj):
    """ For special characters in author names, replace &$x-; with  printable characters """
    t = matchobj.group(0)
    u = (t[3:len(t)-1])   #poor man's regex
    v = (int(u, base=16)) #decode
    return chr(v)         #encode and return

def parseRss(url='https://arxiv.org/rss/physics.optics'):
    """ RSS Feed URL -> list of dictionaries for first five articles

    This function returns a list of dictionaries with the keys 'abstract', 'articleId', 'authors', 'title', and 'url'
    for the first five articles on the specified arXiv RSS Feed url.

    The values for each of the five keys must be strings.

    The string for the authors key should parse the list of authors received from the feed into one single string.

    The default argument url='https://arxiv.org/rss/physics.optics' shows an example of the expected input.
    """

    #YOUR CODE HERE: programmatically producing the articleList of dictionaries described above
    d = feedparser.parse(url)
    num_entries = min(len(d['entries']),5)
    articlesList = [{}]
    for i in range(num_entries):
        summary = d['entries'][i]['summary']
        summary = re.sub('<.*>', '', summary)
        articleId = re.findall('[0-9]+.[0-9]+', d['entries'][i]['id'])[0]
        authors = d['entries'][i]['authors'][0]['name']
        authors = re.sub('<.*?>', '', authors)
        authors = re.sub('&#x.*;', special_repl, authors)
        title = re.findall('[^(]+', d['entries'][i]['title'])[0]
        title = re.sub('\$-\$', '-', title) #encountered this once
        url = d['entries'][i]['link']
        articlesList[i]['summary'] = summary
        articlesList[i]['articleId'] = articleId
        articlesList[i]['authors'] = authors
        articlesList[i]['title'] = title
        articlesList[i]['url'] = url
        articlesList.append({})
    print(articlesList)
    return articlesList

url = 'https://arxiv.org/rss/eess.SP'
t = parseRss(url)

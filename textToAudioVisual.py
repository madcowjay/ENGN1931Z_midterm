# This library takes an article list and generates mp3's and png's for the podcast.
#
#       Jason Webster
#    ENGN 1931Z Spring 2018

from gtts import gTTS
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import random

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'

def createAudioFiles(articlesList=exampleArticlesList, directoryPath=exampleDirectory):
    """  list of article dictionaries ->
    For each article, create an MP3 audio file that includes title, authors, and abstract.
    MP3 files should be stored in the specified directoryPath.
    """
    for article in articlesList:
        text = 'Title........   ' + article['title'] + '........Authors........   ' + article['authors'] + '........Abstract........   ' + article['abstract']
        tts = gTTS(text, lang = 'en')
        tts.save(directoryPath + '/' + article['articleId'] + '.mp3')


def createWordCloudImages(articlesList=exampleArticlesList, directoryPath=exampleDirectory):
    """ list of article dictionaries ->
    For each article, create a square PNG image file using the words from the abstract.
    PNG files should be stored in the specified directoryPath.
    """
    #Carefully curated color combos - as pairs, they will be randomized
    colors =  ['bisque', 'cornflowerblue', 'lightcoral', 'black',  'indigo' ]
    maps   =  ['ocean',  'Greys',          'gist_ncar',  'copper', 'Pastel2']
    indices = [0, 1, 2, 3, 4]
    random.shuffle(indices)

    i = 0
    mask = np.array(Image.open('/home/engn1931z51/mysite/cloud2.png'))
    for article in articlesList:
        wc = WordCloud(height = 2400, width = 2400, background_color = colors[indices[i]], colormap=maps[indices[i]], mask = mask, scale=1)
        wc.generate(article['abstract'].upper())
        wc.to_file(directoryPath + '/' + article['articleId'] + '.png')
        i += 1

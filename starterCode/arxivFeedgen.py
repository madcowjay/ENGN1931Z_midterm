import os
from feedgen.feed import FeedGenerator

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'
def generateRss(articlesList=exampleArticlesList,directoryPath='public_files',baseUrl='https://engn1931z99.pythonanywhere.com/'): 

  """  list of article dictionaries -> 
  Create a feed, which contains all the entries (1 entry for each article in articlesList), with all the information as requested.
  The RSS file should be saved in the specified directory.
  """

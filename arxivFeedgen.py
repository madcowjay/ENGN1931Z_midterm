# This library builds the RSS feed for the podcast.
#
#       Jason Webster
#    ENGN 1931Z Spring 2018


import os
from feedgen.feed import FeedGenerator
import datetime
from mutagen.mp3 import MP3

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'

def generateRss(articlesList=exampleArticlesList,directoryPath='public_files',baseUrl='https://engn1931z99.pythonanywhere.com/'):

    """  list of article dictionaries ->
    Create a feed, which contains all the entries (1 entry for each article in articlesList), with all the information as requested.
    The RSS file should be saved in the specified directory.
    """

    # following method from http://lkiesow.github.io/python-feedgen/ for overall generation
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title('arXiv.org EE SP RSS Podcast')
    fg.link(href = baseUrl)
    fg.language('en')

    #get most recent image for the main podcast picture
    images = sorted([ f for f in os.listdir(directoryPath) if f.endswith('.png')]) #method adapted from https://stackoverflow.com/questions/9788119/how-to-get-the-most-recent-file
    most_recent_image = images[-1]
    fg.logo(baseUrl + 'files?filename=' + most_recent_image) #posts to image as well as logo

    fg.author({'name':'Jason Webster', 'email':'jason_webster@brown.edu'})
    fg.podcast.itunes_owner('Jason Webster', 'jason_webster@brown.edu')
    fg.podcast.itunes_category('Science & Medicine', 'Natural Sciences')
    fg.description('The Best Podcast in the Universe')
    fg.skipDays('Saturday', 'Sunday')

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    fg.pubDate(now)

    for article in articlesList:
        fe = fg.add_entry()
        mp3 = article['articleId'] + '.mp3'
        png = article['articleId'] + '.png'
        fe.id(baseUrl + 'files?filename=' + mp3)
        fe.title(article['title'])
        fe.enclosure(baseUrl + 'files?filename=' + mp3, str(os.path.getsize(directoryPath + '/' + mp3)), 'audio/mpeg')
        fe.description('Authors: ' + article['authors'] + '\n' +
                        'Article Id: ' + article['articleId'] + '\n' +
                        'Abstract: ' + article['abstract'] + '\n')
        fe.podcast.itunes_explicit('clean')
        fe.podcast.itunes_image(baseUrl + 'files?filename=' + png)
        fe.pubdate(now)
        mp3_file = MP3(directoryPath + '/' + article['articleId'] + '.mp3')

        duration = str(datetime.timedelta(seconds = int(mp3_file.info.length)))
        fe.podcast.itunes_duration(duration)

    fg.rss_file(directoryPath + '/podcast.xml', pretty=True)

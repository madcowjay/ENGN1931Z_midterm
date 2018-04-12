# This program builds a podcast from an arxiv.org's rss feed turning text into audio.
#   It uses a webapp on Google AppScripts to get around the onetime exclusion of
#   arxiv.org from pythonanywhere's whitelist.
#
#       Jason Webster
#    ENGN 1931Z Spring 2018

from arxivParser import parseRss
from textToAudioVisual import createAudioFiles, createWordCloudImages
from arxivFeedgen import generateRss

# you can take care of the rest...
end_game = 'https://arxiv.org/rss/eess.SP'
man_in_the_middle = 'https://script.google.com/macros/s/AKfycbxnCZaPPxwOKm8Q6i-XWkJ1gxx8a4bLB3T85mBk6LGj7koQqbDz/exec'
url = man_in_the_middle + '?url=' + end_game
print(url)

baseUrl = 'https://engn1931z51.pythonanywhere.com/'

directoryPath = '/home/engn1931z51/mysite/public_files'

articlesList = parseRss(url)
print('hi')

createAudioFiles(articlesList, directoryPath)
print('mom')
createWordCloudImages(articlesList, directoryPath)
print('testing...')
generateRss(articlesList, directoryPath, baseUrl)
print("totes m'goats")
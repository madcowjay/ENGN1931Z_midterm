# 2018 ENGN1931Z Midterm Exam: Your Own Daily Podcast

# Instructions

This examination is an individual take-home assignment.  You may not discuss the exam or its contents with anyone (except for Professor Zia and the Graduate TAs David and Matthew). 

This examination is an open-book, open-notes, open-web assessment.  You are welcome to use information you may find in books, in your notes, or on the internet; however, *you are* **not** *allowed to actively solicit information*. For example, you are welcome to look for relevant information on StackExchange, but you **cannnot** post on StackExchange requesting help.  

**Please remember that you may not solicit help from others in any way. This exam must be the product of your own independent work, and all exams will be compared for similarities.** Please comment and reference any code that you adapt from online sources.


# Duration and Submission

The exam will be due by 5pm on Thursday April 12th.

1. Please submit a single ZIP file via CANVAS containing archival versions of your work (e.g. \*.js files for javascript, \*.py files for python, \*.text or \*.pdf files for text explanations).  You are welcome to also submit any additional handwritten work for all questions; this work may be submitted as a part of the electronic files as a photo JPEG or scanned PDF.

2. Please also ensure that all of your submission files are stored in the 'mysite' folder of your engn1931z PythonAnywhere accounts.  

# Goal and Context:
In the course, we have learned how to access, distribute, and parse information as well as how to interface discrete systems. With this exam, we would like to show how you can integrate these skills to control and curate the information you receive in your daily life.

For many of us, our mobile phones are our main links to news (e.g., from websites, media apps, podcasts), but the information in which we are most interested doesn't always come in the format we want. This is where automation can help us find the information we want most, reshape it into a form we like, and deliver it to us everyday.

As an example of what is possible with automation, this exam will take you through the six steps of building your very own free (week)daily podcast feed. The primary source of information will be an RSS News Feed on the [arXiv preprint server](http://arxiv.org), and the primary output will be an RSS Podcast Feed (together with associated MP3 audio files and PNG images) served by your own Flask web app. This will allow your mobile phone to continuously sync with audio podcasts describing the new arXiv preprints that are uploaded everyday.

*Please note that the questions below are ordered sequentially based on the steps I used to first build this tool. However, all problems are independent, so you may complete them in any order. Approximate point values are included in the problem headings to help gauge difficulty and value. (I would encourage you to carefully read through all questions before starting.)*

# Problem 1: Parse RSS News Feed (15 points)

We will need to parse relevant information from the arXiv news feed. Select one of the topical categories/classes on [arxiv.org](https://arxiv.org), and then use the [news feed instructions](https://arxiv.org/help/rss) to parse the corresponding url for the RSS feed. I would encourage you to use the python [feedparser](https://pythonhosted.org/feedparser/introduction.html) module together with your favorite tools (e.g., regex and/or BeautifulSoup).

Please complete the `parseRss()` function in the `arxivParser.py` starter file. This function takes as its sole argument a URL (e.g., `http://arxiv.org/rss/physics.optics`) and should return a list of dictionaries (one for each of the first five articles) with the following five keys: 

* abstract: A string containing the article abstract in plaintext **without any html formatting** (e.g., `In 1936, Albert Einstein wrote a brief article where he suggested the possibility that a massive object acted as a lens...`
* articleId: A string containing the article's arXiv id number (e.g., `1801.00001`)
* authors: A string containing comma separated authors names in plaintext (e.g., `Jane Smith, J. J. Doe, J. Carberry`)
* title: A string containing the article title in plaintext (e.g., `Studies of Fireflies in Space`)
* url: A string containing the article's abstract URL (e.g., `http://arxiv.org/abs/1803.00001`)

**Note that all dictionary values should be strings in plaintext (without any html formatting).** 


# Problem 2: Whitelist Web App (15 points)

We will need to create a Google Apps Script web app that takes a URL as its query parameter, requests that URL's contents, and serves them back as text. This seems redundant but is necessary, because our accounts on PythonAnywhere are restricted to communicating with a [limited set of websites](https://www.pythonanywhere.com/whitelist/). While arxiv.org is inaccessible, the Google Apps Script domain (script.googleusercontent.com) is on the so-called whitelist. 

Please create and deploy a Google Apps Script web app that responds to HTTP GET requests that include a 'url' query parameter. If the 'url' parameter begins with `https://arxiv.org`, the web app should return the full content of the specified URL as text. Otherwise, the web app should return an appropriate error message.

**Please include your web app's deployed URL in a comment at the top of your Apps-Script (see `serveItApp.js` starter code), and please make sure to submit your updated `serveItApp.js` file in your Canvas and PythonAnywhere submissions.**

*Ethical & Pedagogical Note: The proper way to address this issue is to request that arxiv.org be added to the whitelist (which we have done so as to help others in the future), but since this is a common interface issue that you can/will encounter, we wanted to ensure you are prepared to implement your own temporary solutions.* 


# Problem 3: Text-to-AudioVisuals (20 points)

We will need to convert the text information into MP3 audio files for the podcast. At the same time, we can also use this text information to produce word clouds that can quickly communicate the main topics of each article. For these purposes, we will use the [gTTS](https://github.com/pndurette/gTTS) python module for the Google Text-to-Speech (TTS) API and the [Word Cloud](https://github.com/amueller/word_cloud) python module.

Please complete the `createAudioFiles()` and `createWordCloudImages()` functions in the `textToAudioVisual.py` file. Both functions should take as arguments an `articlesList` (as described in Problem 1) together with a `directoryPath`. The `createAudioFiles()` function should produce a set of MP3 files (one for each article in the `articlesList`); likewise, `createWordCloudImages()` should produce a set of square PNG images (one for each article based on the text in the abstract and title). In both cases, the files should be saved in 
`directoryPath`.

**Please note that the starter code includes a sample `articlesList` that can be used to test your functions in case you wish to work on this part before completing Problem 1.**

# Problem 4: Generate Podcast RSS Feed (15 points)

In order for our phones to be able to subscribe to our podcast, we will need to produce an RSS feed that combines the text info with appropriate links to the related audio and image files. For this purpose, we will use the [feedgen](https://github.com/lkiesow/python-feedgen) python module. 

Please complete the `generateRss()` function in the `arxivFeedgen.py` file. This function takes as arguments an `articlesList` together with `directoryPath` (that specifies the location of the associated audio and images files) and `baseUrl` (that specifies the url of your PythonAnywhere Flask web app). This function should generate a **valid RSS 2.0** podcast file that includes separate episodes for each article. The generated RSS should be saved as `podcast.xml` in the specified directory.

Please ensure that the podcast **feed** in the RSS includes, at least, the following tags: `title`, `link`, `language`, `image`, `itunes:email`, and `itunes:category`. (For the podcast `image`, please use one of the Word Clouds URLs.)

Furthermore, please ensure that each **episode item** includes, at least, the following tags: `enclosure`, `title`, `description`, `link`, `itunes:explicit`, and `itunes:image`. (Note that the `enclosure` tag should include the filesize `length` in bytes. The `description` should contain the authors and abstract of the article. The `itunes:image` should be the Word Cloud URL for that article, and the `link` should be the arXiv abstract URL.)

# Problem 5: Serve Files from Flask (15 points)

We will need a publicly accessible website to distribute our RSS feed and related files. For this purpose, we will use a [Flask](https://help.pythonanywhere.com/pages/Flask/) web app from our PythonAnywhere accounts. The web app should include two routes: `files` for serving PNG images and MP3 audio files, and `rss` for serving the podcast's XML. 

Please complete the `serveFile()` and `serveRss()` functions in the `flask_app.py` file. The `serveFile()` function should parse the filename query parameter and serve the appropriate file, whereas the `serveRss()` function simply serves the podcast's XML file without any need for query paramters. 

Note that all these files should be **stored in the `public_files` directory** located within `mysite`. To serve the files in Flask, please use the `send_from_directory()` method that was discussed in class this week.

Note that all files **must** be served with the correct Content-Type [MIME](https://www.wikiwand.com/en/Media_type) header to ensure that the bytes stream can be correctly interpreted.

*Technical Note: Ideally our website should be able to serve requested portions of a file (based on a bytes-range request). However, setting this up in Flask is outside the bounds of this exam. The basic settings in Flask should allow you to access the files, but you may encounter issues with some podcast apps. To test out your integration in the following, we would encourage you to use one of the following apps that we have validated. (See Note in Problem 6.)*


# Problem 6: Integration and Automation (20 points)

We are now ready to combine all the pieces above into a single automated process that queries the arXiv RSS feed through your Apps Script web app, parses the relevant info, and creates the MP3/PNG/XML files. We also setup the server that will serve these files over the internet.

Please complete the `podcastBuilder.py` script. This script begins by importing the functions from your other files (`arxivParser.py`, `textToAudioVisual.py`, `arxivFeedgen.py`). **Please be sure to test this script first on your OWN COMPUTER before proceeding to cloud deployment,** because you have limited CPU time each day on PythonAnywhere.

#### PythonAnywere Cloud Deployment

Once you have successfully tested your `podcastBuilder.py` script on your computer, please upload all the script files to your `mysite` directory on PythonAnywhere. In total, there should be six files: `arxivFeedgen.py`, `arxivParser.py`, `flask_app.py`, `podcastBuilder.py`, `serveItApp.js`, and `textToAudioVisual.py`. You should also create a `public_files` directory within `mysite` to store the MP3, PNG, and XML files.

#### Manual Testing
Manually test your `podcastBuilder.py` script within a Bash console on PythonAnywhere. Since we are using libraries beyond those automatically included on PythonAnywhere, you will need to run this script within the virtual environment `myvirtualenv` where you have pip installed all the requisite packages. Note that you have a limited CPU time in PythonAnywhere, so begin by doing small tests (on only one article for example), and scale it up when you're sure this works.

Confirm that you can subscribe and listen to your podcast via mobile phone. To do this, enter your podcast RSS feed URL (e.g., `http://engn1931z##.pythonanywhere.com/rss`) on your favorite podcast app. **Since we have not implement byte-range requests, some apps may have problems.** For iOS, the basic Podcasts app will allow you to access audio once, but may not work consistently. **Therefore, we would recommend testing with one of the following free apps that we have tested and validated: the iOS [Overcast](https://itunes.apple.com/us/app/overcast/id888422857?mt=8) app or the Android [Castbox](https://play.google.com/store/apps/details?id=fm.castbox.audiobook.radio.podcast&hl=en_US) app.** This is not critical for your final grade, and there should be many other apps that work. If you have any problems with these apps (e.g. with compatibility), please email us and we can find other options.

#### Automatic Scheduling
Once you know that everything is working, we will want to schedule the `podcastBuilder.py` to run once each day (e.g. at 00:30 UTC since the arXiv updates daily at 00:00 UTC). To do this read [here](https://help.pythonanywhere.com/pages/ScheduledTasks/).

After testing and scheduling, your podcast feed should update by itself, and in turn, you phone will sync a new set of arXiv audio episodes each day. Kick back and enjoy the tunes (sort-of)! And if you are motivated, you can always redirect the tools above to any other text RSS news feed you like....

# Good Luck!

<p align="center">
<img src="https://github.com/engn1931z/draft/blob/master/podcast.JPG?raw=true" alt="Podcast" width="500">
 </p>

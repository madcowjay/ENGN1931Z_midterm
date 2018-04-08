import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/files')
def serveFile():
    """ Serve the requested file (mp3/png)
    This function receives a filename in the form of a query string (e.g. /files?filename=image.png), and serves the corresponding file in the `public_files` directory (e.g. mysite/public_files/image.png).
    """    
    if # the requested file is mp3
        # Serve the requested mp3
        return
    elif # the requested file is png
        # Serve the requested png
        return

@app.route('/rss')
def serveRss():
    """ Return the podcast RSS generated
    """
    #YOUR CODE HERE promgrammatically serve the podcast RSS generated
    return

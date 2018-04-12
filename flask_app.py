# This website is a simple podcast file server - it serves the RSS, mp3, and png files.
#
#       Jason Webster
#    ENGN 1931Z Spring 2018

from flask import Flask, request, send_from_directory, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def main():
    """ A little landing page based on a flask tutorial
    One image, and one link to the RSS page
    """
    return render_template('index.html')

@app.route('/files')
def serveFile():
    """ Serve the requested file (mp3/png)
    This function receives a filename in the form of a query string (e.g. /files?filename=image.png), and serves the corresponding file in the `public_files` directory (e.g. mysite/public_files/image.png).
    """
    filename = request.args.get('filename')
    l = len(filename)
    if filename[l-3:l] == 'mp3':
        # Serve the requested mp3
        return send_from_directory('public_files', filename, mimetype = 'audio/mpeg')
    elif filename[l-3:l] == 'png':
        # Serve the requested png
        return send_from_directory('public_files', filename, mimetype = 'image/png')
    else: return render_template('error.html')

@app.route('/rss')
def serveRss():
    """ Return the podcast RSS generated
    """
    return send_from_directory('public_files', 'podcast.xml', mimetype = 'application/rss+xml')
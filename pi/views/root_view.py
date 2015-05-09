'''
Created on May 8, 2015

@author: Aman
'''
from pi import app
from flask.templating import render_template

@app.route("/")
def hello():
    return render_template('index.html')




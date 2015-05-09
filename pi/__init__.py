'''
Created on May 8, 2015

@author: Aman
'''
from flask import Flask
from flask.templating import render_template
#from flask_mako import render_template
#from flask.ext.mako import MakoTemplates


app = Flask(__name__)
#mako = MakoTemplates(app)

import pi.views.root_view


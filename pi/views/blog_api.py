'''
Created on May 9, 2015

@author: Aman
'''
from pi import app
from flask.templating import render_template
from pi.db.database import db_session
from pi.db.models import Blog
from flask.wrappers import Response
from pi.utils.json_util import toJson

@app.route("/api/v1/blogs", methods=['GET'])
def get_blogs():
    blogs = Blog.query.order_by(Blog.created.desc(), Blog.id.desc()).limit(10).all()
    return Response(toJson(blogs),  mimetype='application/json')

'''
Created on May 9, 2015

@author: Aman
'''
from sqlalchemy.sql.schema import Column

from pi.db.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
import datetime

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    user = Column(String(10))
    blog = Column(String())
    created = Column(DateTime)

    def __init__(self, user=None, blog=None):
        self.user = user
        self.blog = blog
        self.created = datetime.datetime.now()
        
    def __repr__(self):
        return '<User %r>' % (self.user)


class User(Base):
    __tablename__ = 'user'
    id = Column(String(10), primary_key=True)
    email = Column(String(50))
    name = Column(String(25))
    passwd = Column(String(80))
    salt = Column(String(20))
    created = Column(DateTime)

    def __init__(self, id=None, email=None, name=None, passwd=None, salt=None):
        self.id = id
        self.email = email
        self.name = name
        self.passwd = passwd
        self.salt = salt
        self.created = datetime.datetime.now()
        
    def __repr__(self):
        return '<User %r>' % (self.id)
        
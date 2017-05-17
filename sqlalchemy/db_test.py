#! /usr/bin/env python

import flask
import flask_restless
import flask_sqlalchemy
from sqlalchemy.dialects import mysql
import uuid


app = flask.Flask('db_test')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_test:password@localhost/db_test'
db = flask_sqlalchemy.SQLAlchemy(app)

class Fractal(db.Model):
    uuid = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    
    def __init__(self,uuid,name):
        self.uuid=uuid
        self.username=name

    def __repr__(self):
        return '<Fractal %s>' % self.uuid

db.create_all()
#manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

admin = Fractal(str(uuid.uuid4()),'admin')
guest = Fractal(str(uuid.uuid4()),'guest')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

users=Fractal.query.all()
print users



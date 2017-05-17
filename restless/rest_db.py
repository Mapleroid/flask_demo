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

    def __repr__(self):
        return '<Fractal %s>' % self.uuid

db.create_all()
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Fractal, methods=['GET', 'POST', 'DELETE', 'PUT'],
                    url_prefix='/v1')
app.run(host="0.0.0.0", port=80)


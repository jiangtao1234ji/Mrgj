#!/usr/bin/python
# -*- coding:utf8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = 'i am jiangtao! do you know?'
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:18652411ji@localhost/mrgj?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# app.config["DATABASE"] = os.path.join(APPS_DIR, 'database.db')

APPS_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(APPS_DIR, 'static')
app.config["UPLOADS_RELATIVE"] = 'uploads'
app.config["UPLOADS_FOLDER"] = os.path.join(STATIC_DIR, app.config["UPLOADS_RELATIVE"])

app.config["UPLOADED_PHOTOS_DEST"] = app.config["UPLOADS_FOLDER"]

import apps.views

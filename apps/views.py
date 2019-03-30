from flask import render_template, request

from apps import app
from apps.models import MrgjTag, Mrgj


@app.route('/', methods=["GET"])
def index():
    mrgj_tags = MrgjTag.query.all()
    mrgjs = Mrgj.query.paginate(per_page=6)
    return render_template('index.html', mrgj_tags=mrgj_tags, mrgjs=mrgjs)

@app.route('/list<int:page>', methods=["GET"])
def list(page):
    mrgj_tags = MrgjTag.query.all()
    mrgjs = Mrgj.query.paginate(page=page, per_page=6)
    return render_template('list.html', mrgj_tags=mrgj_tags, mrgjs=mrgjs)

# @app.route('/index<int:page>', methods=["GET"])
# def browse(page):
#     mrgj_tags = MrgjTag.query.all()
#     mrgjs = Mrgj.query.filter(Mrgj.tag_id == MrgjTag.id)
from datetime import datetime

from apps import db


class Mrgj(db.Model):
    __tablename__ = 'mrgj'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.TEXT)
    href = db.Column(db.String(80), unique=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('mrgj_tag.id'))

    def __repr__(self):
        return '<Mrgj %r>' % self.name


class MrgjTag(db.Model):
    __tablename__ = 'mrgj_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    mrgjs = db.relationship('Mrgj', backref='mrgj_tag')

    def __repr__(self):
        return '<MrgjTag %r>' % self.name


if __name__ == "__main__":
    flag = 1
    if flag == 0:
        db.drop_all()
        db.create_all()
    if flag == 1:
        # tag0 = MrgjTag(name='东晋')
        # tag1 = MrgjTag(name='宋朝')
        # tag2 = MrgjTag(name='明朝')
        # tag3 = MrgjTag(name='清朝')
        # tag4 = MrgjTag(name='近代')
        # db.session.add(tag0)
        # db.session.add(tag1)
        # db.session.add(tag2)
        # db.session.add(tag3)
        # db.session.add(tag4)
        # db.session.commit()

        mrgj = Mrgj(name='汪精卫公馆旧址', desc='汪精卫公馆旧址位于中国江苏省南京市鼓楼区颐和路38号(西康路46-2号，原颐和路34号)，邻近美国驻中华民国大使馆旧址，为汪精卫1940年-1944年任"中华民国国民政府"主席兼行政院院长时所居住的别墅。汪精卫公馆旧址位于中国江苏省南京市鼓楼区颐和路38号(西康路46-2号，原颐和路34号)，邻近美国驻中华民国大使馆旧址，为汪精卫1940年-1944年任"中华民国国民政府"主席兼行政院院长时所居住的别墅。该建筑由褚民谊所赠，抗日战争胜利后由国民党战地服务团接收并一度作为美军军官俱乐部，目前由南京军区管理使用。',
                    href='https://baike.so.com/doc/2433680-2572727.html', tag_id=5)
        db.session.add(mrgj)
        db.session.commit()



#coding=utf-8

from datetime import datetime
from .database import db

'''
    model模块
    数据库列表的束腰信息，imgsrc--妹子照片的网址  title--妹子照片的主题  topiclink--  startcount--星
    数据库表名--meizi
'''
def dump_datetime(value):
    ''' deserialize datetime object into string form for JSON process '''
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%s")]

class MeiZiModel(db.Model):
    __tablename__ = "meizi"
    id = db.Column(db.Integer, primary_key=True)
    imgsrc = db.Column(db.String(300))
    title = db.Column(db.String(300))
    topiclink = db.Column(db.String(300))
    startcount = db.Column(db.String(100))
    pub_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, imgsrc, title, topiclink, startcount, pub_time=None):
        self.imgsrc = imgsrc
        self.title = title
        self.topiclink = topiclink
        self.startcount = startcount
        if pub_time:
            self.pub_time = pub_time

    def __repr__(self):
        return '<MeiZi %r>' % self.imgsrc

    @property
    def serialize(self):
        '''return object data in easily serialzeable format'''
        return {
            'id':           self.id,
            'imgsrc':       self.imgsrc,
            'title':        self.title,
            'topiclink':    self.topiclink,
            'startcount':   self.startcount,
            'pub_time':     dump_datetime(self.pub_time)
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    aid = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    url = Column(String)
    author = Column(String)
    content = Column(String)
    publish_time = Column(String)
    source_site = Column(String)
    extra1 = Column(String)
    extra2 = Column(String)
    extra3 = Column(String)


class ArticleWithTableName(Article):
    def __init__(self, table_name):
        self.__tablename__ = table_name
        self.aid = Column(Integer, primary_key=True)
        self.title = Column(String)
        self.category = Column(String)
        self.url = Column(String)
        self.author = Column(String)
        self.content = Column(String)
        self.publish_time = Column(String)
        self.source_site = Column(String)
        self.extra1 = Column(String)
        self.extra2 = Column(String)
        self.extra3 = Column(String)

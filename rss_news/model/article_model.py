# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ArticleModel(Base):
    __tablename__ = 'none'

    aid = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    url = Column(String)
    author = Column(String)
    content = Column(String)
    publish_time = Column(TIMESTAMP)
    source_site = Column(String)
    extra1 = Column(String)
    extra2 = Column(String)
    extra3 = Column(String)

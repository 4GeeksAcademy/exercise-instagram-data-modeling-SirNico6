import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum as PyEnum


Base = declarative_base()

class User(Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)

class Follower(Base):
    __tablename__ = 'FOLLOWER'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('USER.id'))
    user_to_id = Column(Integer, ForeignKey('USER.id'))
   
    def to_dict(self):
        return {}
    
class Post(Base):
    __tablename__ = 'POST'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id'))
    author = relationship(User)

class Comment(Base):
    __tablename__ = 'COMMENT'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('USER.id'))
    post_id = Column(Integer, ForeignKey('POST.id'))
    author = relationship(User)

class MediaType(PyEnum):
    STORY = 'STORY'
    REEL = 'REEL'
    PICTURE = 'PICTURE'
    
class Media(Base):
    __tablename__ = 'MEDIA'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('POST.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
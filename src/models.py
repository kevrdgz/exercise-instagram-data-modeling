import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Enum , UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email  = Column(String(250),nullable=False, unique=True)

class Followers(Base):
    __tablename__  = 'followers'
    id = Column(Integer, primary_key= True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    mediatype = Column(Enum('video','photo'))
    url = Column(String(250))
   

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
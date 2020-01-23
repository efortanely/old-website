from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class BlogPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    date = Column(String(15))
    content = Column(String(3000))

engine = create_engine('sqlite:///blog_posts.db')
Base.metadata.create_all(engine)
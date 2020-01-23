from flask_frozen import Freezer
from main_app import app
from database_setup import Base, BlogPost
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///blog_posts.db')
Base.metadata.bind = engine

freezer = Freezer(app)

@freezer.register_generator
def blogPost():
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    for post in session.query(BlogPost).all():
        yield {'post_date': post.date, 'post_title': post.title.replace(' ','-')}

if __name__ == '__main__':
    freezer.freeze()
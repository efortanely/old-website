from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import BlogPost, Base
from html_generator import generate_html

engine = create_engine('sqlite:///blog_posts.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_post = BlogPost(
    title="Introduction", 
    date="2020-1-23", 
    content="Hello everyone!<br><br>Today is the first day of my blog being up and running :D \
        After lots of fiddling with Jekyll and eventually giving up, I finally found (what \
        I hope to be a solution, haven't yet deployed to GitHub Pages) Frozen Flask to be \
        something that finally worked.<br><br>I've had this webpage as just a static one-pager \
        for a while now and I was excited to integrate Flask into it and add a database. \
        Although my solution isn't beautiful, I'm glad to at least have something to call \
        my own. For now this will primarily be used for blogging for my Software Engineering \
        class (gotta get that writing flag!), but I'm hoping along the way I can also use this \
        as a landing page for thoughts about personal projects, hackathons, or anything else \
        interesting that comes up with me :) <br><br>That's all for now, have a good day!"
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

generate_html()

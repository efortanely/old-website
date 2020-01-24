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
    date="1-23-2020", 
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

new_post = BlogPost(
    title="First Iteration of the Stuart Bot!", 
    date="1-24-2020", 
    content="So I finally got a prototype of the Stuart Bot working that \
    I'm happy with! If you're not sure what I'm talking about, the Stuart Bot is \
    essentially a webcam I have pointed at my boyfriend's apartment's resident cat \
    and it takes a picture of him every so often. I'm soon to be moving in with them, \
    so this very may well be quite a long-term project!<br><br>I was having some issues \
    with finding a model that would work well for this. At first I was trying to use a pre-trained \
    model in OpenCV as per <a href='https://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/'>this tutorial</a>. \
    I was having a lot of difficulty having it even detect Stuart and got a couple of positives, but \
    other than that, just not a lot of luck. Finally I switched over to ResNet-50 and this was great, \
    because where the OpenCV model could only (barely) detect only cat faces, ResNet-50 was really good \
    at detecting faces and bodies from all sorts of perspectives. This made it a lot easier for the twitter bot \
    to work since Stuart usually sits in weird contorted positions in the bean bag, haha.<br><br> If you \
    want to check out the code it's in this <a href='https://github.com/codesmary/Stuart-Bot'>repo</a> and if you \
    just want to look at cute cat pictures the twitter bot can be found <a href='https://twitter.com/TheStuartBot'>here</a>."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

generate_html()

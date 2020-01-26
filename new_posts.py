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

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely", 
    date="1-25-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'> Okay, so I guess this is the part \
        where I talk about myself. I grew up in the Austin area, but more specifically Pflugerville for people \
        that are actually from the Austin area. I went to three high schools (whee!), Pflugerville \
        High School, then Texas Connections Academy, then Pflugerville again, and then Hendrickson High \
        School. During this time I spent a lot of time not being particularly academically interested, until \
        I took a physics class and realized that problem solving was actually something I found quite exciting. \
        After this point I was in a handful of activities: Art club, Karate, and UIL CS/Math. I actually ended \
        up coming to UT after being CAPped to UT Arlington for a year and somehow managed to transfer in. I was \
        one of the lucky ones, I guess! I'm majoring in CS because I thought I wanted to be a EE major after my \
        physics courses, but then realized CS is a lot cooler, haha. Thanks older brother!\
        <br><br>I'm taking SWE because I heard Downing was a professor that was a 'must-take'. \
        I think I'm already pretty well-versed with full-stack web apps. I built this website and am generally pretty \
        good with Flask/Database technologies/HTML/CSS. I think the only thing I'm weaker on is React and JS related \
        web technologies. I thought the first couple of lectures were fine. I was mostly dredding getting cold called, \
        but that hasn't happened yet! \
        <br><br>I'm having a pretty good time because I'm currently at TAMUhack. Although I'm dreading \
        what the sleep situation will be like since my Airbnb fell through, I'm quite happy with what \
        I've accomplished. It's a tool that's meant to help blind people, a <a \
        href='https://github.com/codesmary/PixReader'>screen reader</a> that not only reads text, but also 'reads' \
        images through the use of computer vision. I finished my project within the first 5 hours, so now I'm just \
        working on this blog post, haha. That was pretty satisfying since I've never finished such a lofty project so \
        fast! \
        <br><br>My tip of the week is don't trust everything you see online. I was trying to use a \
        pretrained model that seemed to provide great results on the blog post about it, but after I \
        spent forever trying to get it to work, it output captions for images as primitive as 'adult' \
        and 'cat'. Such a bummer."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

generate_html()

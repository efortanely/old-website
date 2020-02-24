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

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Jan. 27", 
    date="2-2-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>Hello everyone! My past week was \
    pretty good, I finally got my Collatz implementation working on Hackerrank. It was easy to get it \
    working, but much harder to add caching and get it efficient enough to pass all three tests. I was \
    disappointed to find with all the effort I put into the meta-cache, that it slowed down my implementation \
    so much that it failed the second test, and once I removed it, my code was fast enough to pass it again. \
    There were certainly some points where I felt like I just wanted to give up, but the tips we went over in \
    class and the encouragement from my peers really helped. \
    <br><br><b>2. What's in your way?</b>\
    <br><br>Realistically, the only thing in my way is my willingness to work, but I'm pushing through it!\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>At this point, I've finished the main objective of the assignment, that is, creating a cached \
    implementation that will find maximum Collatz cycle lengths for a number of ranges. Now I just need to \
    refactor my code, do testing, and all the other tasks we reviewed in order to closer adhere to the workflow \
    for this class. \
    <br><br><b>4. What was your experience with assertions, unit tests, coverage, and continuous integration?</b>\
    <br><br>I've had experience with all the technologies we talked about this week, but found myself most \
    comfortable with assertions, as I've worked with them for other classes (primarily in Java), unit tests, \
    as I've had to create this for previous internships, and continuous integration, as I've found this to be \
    standard at most places I've worked. It will be interesting to be looking at code coverage in python and \
    learn more about that. \
    <br><br><b>5. What made you happy this week?</b>\
    <img src='/static/city-gouache.jpg' align='left' class='border'> \
    <br><br>I was happy that I finished a gouache \
    painting for the first time since last summer. I still have more practice to do since I was hoping for a \
    more impressionistic style, but that will just take time (and possibly new brushes)! \
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>My pick-of-the-week is laser printing! I found it be a very powerful tool that complements any sort of \
    encasing you'll need to do for hardware. Just create a box using any online tool and edit to have whatever \
    sorts of features you need and you're done! I worked with a friend this week to create a prototype box to \
    hold some hardware for a cat bot I've been working on, and it was a really fun process."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Feb. 3", 
    date="2-9-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>Over this past week, I finished the Collatz project. This involved writing the 15 issues, unit \
    and acceptance tests, and plugging in my code I had written for Hackerrank into Downing's boilerplate \
    code. The whole project took me about 5 hours to finish. \
    <br><br><b>2. What's in your way?</b>\
    <br><br>I didn't have too many issues with completing these tasks as they weren't as intensive as writing \
    the code to solve the problem itself. The main thing I had a little bit of trouble with was determining \
    how to write a unit test that could catch when the code threw a certain exception, but after enough \
    Googling I figured that out! \
    <br><br><b>3. What will you do next week?</b>\
    <br><br>I need to review the notes from Friday with a friend as I had to miss that class, and then I \
    will begin the second project with my team. I'm excited to get into the meat of this class!\
    <br><br><b>4. What was your experience of exceptions, types, and operators?</b>\
    <br><br>I generally find myself using exceptions in code I write for hobby because they are a pretty \
    helpful tool to trigger certain behaviours if the code breaks and makes debugging much easier. As for \
    python types and operators, I consider myself pretty comfortable with them as I've slowly grown to adopt \
    python as my language of choice. I had, however, never heard of frozenset! It was interesting to learn \
    something new.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>I travelled to Oklahoma this weekend to participate in Hacklahoma (which is also why I missed \
    class Friday, as I mentioned), and really enjoyed my time there! They had great food, a fun origami \
    workshop, and I got to stay in a hotel for a bit and change up my routine. My project I worked on is \
    called SpotYourFriends, a web app that lets you create playlists with you friends that contain songs \
    you all have in common. It does this by finding the intersect of all the songs in each user's library \
    of playlists. It was built with Flask, Spotipy, HTML, CSS, and JavaScript. You can read more about it \
    and check out the repo <a href='https://devpost.com/software/spotyourfriends'>here</a>.\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>My pick-of-the-week is Spotipy, a python wrapper for the Spotify Web API. Although it wasn't \
    perfect, it made working with Spotify for SpotYourFriends pretty easy."

)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Feb. 10", 
    date="2-15-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>Over the past week, I reviewed the operator material I missed last Friday and also started up on \
    research with Connor for one of the project ideas for the upcoming website. We created the scheme for a \
    few models, including the Pet, Breed, and Shelter model, as well as found a Austin Animal Center dataset \
    of information over dog and cat intakes at a local shelter and a couple of APIs about cat and dog breeds, \
    in addition to couple of adoption websites that can be scraped for data to supplement the Austin Animal \
    Center dog and cat dataset.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>Right now the group is mostly just waiting on having our first meeting before we go ahead with \
    anything. Presumably in this meeting we will go over the results from a poll we set up to decide which \
    project proposal we liked the most (a few of us proposed the animal adoption website, the Austin music \
    website, and an exercise sources website), as well as determining what roles each of us want to take \
    going forward for this first part of the project.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>I am not sure exactly which part of the project I will be working on, but my interests in web \
    development probably lean more towards back-end development, but I would like to also improve my skills \
    in front-end development, specifically in React and TypeScript, as well as graphic design.\
    <br><br><b>4. What was your experience of Project #1: Collatz (the problem, the overkill requirements \
    of submission, etc.)?</b>\
    <br><br>I thought Collatz was a fun problem, but I do agree that all of the different tools we had to \
    use and steps we had to go through to go from finishing the Hackerrank problem to turning in the final \
    script and tests was kind of overwhelming. I got through it eventually though, and looking back on it, \
    the hardest part was simply the Hackerrank portion and getting all the tests to pass. I think I just \
    had a less favorable experience with the software engineering side of things because it felt like a \
    bit of drudge work.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>I was having some issues with getting authentication to work with the Spotify API for my \
    SpotYourFriends side project, but I finally got that fixed so I could deploy it to Heroku and now \
    it feels like a real thing instead of just a toy website I run from my terminal, which made me feel \
    really excited!\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>Heroku is a great tool for getting urls and hosting websites. It’s free at a certain tier \
    and very straight forward to use!"

)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Feb. 10", 
    date="2-15-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>Over the past week, I reviewed the operator material I missed last Friday and also started up on \
    research with Connor for one of the project ideas for the upcoming website. We created the scheme for a \
    few models, including the Pet, Breed, and Shelter model, as well as found a Austin Animal Center dataset \
    of information over dog and cat intakes at a local shelter and a couple of APIs about cat and dog breeds, \
    in addition to couple of adoption websites that can be scraped for data to supplement the Austin Animal \
    Center dog and cat dataset.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>Right now the group is mostly just waiting on having our first meeting before we go ahead with \
    anything. Presumably in this meeting we will go over the results from a poll we set up to decide which \
    project proposal we liked the most (a few of us proposed the animal adoption website, the Austin music \
    website, and an exercise sources website), as well as determining what roles each of us want to take \
    going forward for this first part of the project.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>I am not sure exactly which part of the project I will be working on, but my interests in web \
    development probably lean more towards back-end development, but I would like to also improve my skills \
    in front-end development, specifically in React and TypeScript, as well as graphic design.\
    <br><br><b>4. What was your experience of Project #1: Collatz (the problem, the overkill requirements \
    of submission, etc.)?</b>\
    <br><br>I thought Collatz was a fun problem, but I do agree that all of the different tools we had to \
    use and steps we had to go through to go from finishing the Hackerrank problem to turning in the final \
    script and tests was kind of overwhelming. I got through it eventually though, and looking back on it, \
    the hardest part was simply the Hackerrank portion and getting all the tests to pass. I think I just \
    had a less favorable experience with the software engineering side of things because it felt like a \
    bit of drudge work.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>I was having some issues with getting authentication to work with the Spotify API for my \
    SpotYourFriends side project, but I finally got that fixed so I could deploy it to Heroku and now \
    it feels like a real thing instead of just a toy website I run from my terminal, which made me feel \
    really excited!\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>Heroku is a great tool for getting urls and hosting websites. It’s free at a certain tier \
    and very straight forward to use!"

)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Feb. 17", 
    date="2-23-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>This past week I’ve been doing a lot of graphic design work and front-end development for \
    our website. I’ve designed the home page, the about page, and the search page, as well as completed \
    the corresponding code for those, sans the search page. It was also my first time creating vector \
    graphics. Even though the designs I made were really simple, I enjoyed learning about that since \
    it’s been a goal of mine for a while to improve on that skill so I can make more engaging websites.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>I think the main thing making it hard to work right now is stress. I like having things done \
    early and it’s been stressing me out not having control over that and waiting for things to fall \
    into place. There’s also been some miscommunication and people haven’t been making issues besides \
    me and Connor which makes it hard to tell who’s working on what.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>At this point, I’m not sure what will be my next work item, if any. I suppose this will be \
    solidified at our meeting we’re having this Monday.\
    <br><br><b>4. What was your experience of iteration, AWS, and Chef Secure?</b>\
    <br><br>I thought some of the tricks we went over during the iteration lecture were neat, such as \
    how an iterator of an iterator will always return an iterator. I was surprised at how much effort \
    goes into hosting since before I had only ever used tools like Heroku and GitHub Pages which made \
    hosting straightforward, so I’m hoping our guys working on hosting can get through that okay. The \
    mini security lecture from the CEO of Chef Secure has given me a new perspective on \
    vulnerabilities online.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>Today, my boyfriend, Connor, and I went to Michi Ramen off Lamar and I got some yummy ramen and \
    fries. Even though we had just been there last week for Valentine’s Day, I still enjoyed it \
    because they have top tier tofu.\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>Marvel App is a nice tool for creating mock-ups that I’ve used for this and a couple of \
    previous web design projects, and I’ve found it helpful to have something a little more concrete \
    than just making a rough sketch on paper."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

generate_html()

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

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Feb. 24", 
    date="3-1-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>I spent the last week helping some of the other people on my team with cleaning \
    up their pages, specifically our model and instance pages. I fixed the layout of the \
    pages and changed the styles to match our theme. I’m hoping we can have an attractive \
    website at the end of this project, and something we can all be proud of.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>Time was the main constraint. It would get stressful when people would put off \
    committing code until closer to the deadline and there would be changes I wanted to \
    make, but minimal time to spend to making them before it had to be done for Phase 1.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>My team is hopefully meeting on Tuesday, and at that point we will be having a \
    retro for Phase 1 and going over the tasks for Phase 2 and breaking them down. My goal \
    is to work on the back-end since I have substantial experience with Flask and \
    SQLAlchemy (I even already use them for this website!)\
    <br><br><b>4. What was your experience of comprehensions, generators, and yield?</b>\
    <br><br>I love comprehensions. I was first exposed to them when I started with \
    competitive programming in python as a Freshman in college and I thought back then it \
    was the coolest thing. I was surprised that map and reduce are implemented as generators \
    just because I don’t use them very often to begin with, and I had never read that before. \
    I had also seen yield before, but didn’t entirely understand the difference between it \
    and ‘return’. I had thought I was already a pretty skilled python developer before this \
    class, but our lectures have been great to learn and show me just how much I didn’t know.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>I just joined the club Freetail Hackers this semester and we put on our spring \
    hackathon, LeapHacks, this last Saturday. I enjoyed getting to help with the program and \
    make new friends while I was there.\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>My pick-of-the-week is the framework we’re required to use for Phase 2’s back-end, \
    Flask! I first set out to learn it after seeing it come up again and again in hackathon \
    projects I’ve seen friends make, and after picking it up, I’ve made many projects with it \
    myself! It’s relatively straightforward to understand, and it’s a great tool for making \
    dynamic web apps with."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Mar. 2", 
    date="3-8-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>I spent the last week working on the back-end implementation for Phase 2 of our IDB project. I \
    have been creating the models for the database, as well as writing our Pets4Me API that will be called \
    by our front-end. Additionally, since there is a test coming up this week, I have been studying old \
    Hackkerank questions for that. Since all of my notes for this class are only about a page long, I’m \
    hoping to be able to condense it all into a nice study sheet for the test before Wednesday.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>I picked up the tasks I did because I had worked with Flask before so I assumed the way the \
    routing for the API would work would be the same, but it ended up being different for Flask-Restless \
    so I had to get accustomed to that. Getting used to that different library was the main obstacle.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>I have to finish writing tests for my API using both unittest and Postman. I feel comfortable \
    that I'll be able to write unit tests since I have experience with modifying the database and getting \
    responses from an API, but I'll need to learn about something called 'stubs' I think to be able to finish \
    those without permanently messing up the database. I'm more worried about using Postman since I haven't \
    written anything using Postman for a couple of years.\
    <br><br><b>4. What was your experience of =, *, **, and decorators?</b>\
    <br><br>I had used = before, but *, **, and decorators were mostly new to me. I had a tough time with the \
    quiz, but I've been studying for the test and I feel confident that I'll be able to nail it then.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>My team got our grade back for Phase 1, and I'm glad we did well on our first project. There were \
    some minor errors, but we discussed them and surely we'll do better next time. We made a pseudo-deadline \
    for a week before the project is due, so hopefully, that'll help us with tying loose ends long before the \
    project is due.\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>My tip of the week is to start early on coding projects! Save yourself the undue stress by giving \
    yourself adequate time to finish the task at hand."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Mar. 9", 
    date="3-15-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. What did you do this past week?</b>\
    <br><br>This last week, I implemented some unit tests in python for the API I worked on the week before last. They were pretty straightforward, just testing status codes for each of the models, but it should get more complicated once more query parameters and filtering are added for the next phase. I also began writing the definition for our API in Postman.\
    <br><br><b>2. What's in your way?</b>\
    <br><br>I will probably be making slow progress on writing the Postman definitions. It’s incredibly tedious. Also, I’m still waiting on one of our hosting guys to help me with troubleshooting getting access to the PostgreSQL database instance, and once that’s working, I can merge my repo and get our back-end in the cloud.\
    <br><br><b>3. What will you do next week?</b>\
    <br><br>I’ll keep working on writing the Postman definitions. Additionally, once the back-end is merged and working, I’ll write the Postman tests for it. I’m hoping the extra week we got thanks to the world ending will help with getting everything done in time.\
    <br><br><b>4. What was your experience of Test #1a?</b>\
    <br><br>I had a hard time with time management for question 2. I spent a long time on question 2 trying to get my way through the solution, and once I finally did that, I was able to do question 3 pretty fast, and then I really didn’t have enough time for finishing question 1. I think Test #1b will go smoother.\
    <br><br><b>5. What made you happy this week?</b>\
    <br><br>Me and my boyfriend went to Sip Pho on Friday since classes were cancelled. I certainly enjoyed that more than taking the second part of our test. It was nice to take a break since we had both been really busy this week with wrapping up everything before spring break started. I wish spring break was a series of holidays spread out over the course of the semester instead of an entire week so this stressful week didn’t need to occur.\
    <br><br><b>6. What's your pick-of-the-week or tip-of-the-week?</b> \
    <br><br>I’ve been using ‘jsonschema.net’ for creating the Postman definitions from my json output from our API. I still pick through the auto generated output to create something a little cleaner, but overall it’s been rather helpful for doing a lot of the work for that portion of the project."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

# post = session.query(BlogPost).filter_by(title="CS373 Spring 2020: Rosemary Fortanely — Week of Mar. 9").one()
# session.delete(post)
# session.commit()

new_post = BlogPost(
    title="CS373 Spring 2020: Rosemary Fortanely — Week of Mar. 16", 
    date="3-28-2020", 
    content="<img src='/static/rosemary.jpeg' align='left' class='border'>\
    <b>1. Are you and your family safe and sound where you are?</b>\
    <br><br>Currently, I am by myself in my studio apartment, but I am doing well. I had a group chat with 8 of my other family members earlier this morning and everyone is currently staying put and coronavirus-free, so I count that as a win.\
    <br><br><b>2. How do feel about your ability to finish the term completely online?</b>\
    <br><br>I’m kind of worried. I don’t have a great track record for online classes, so I hope that’s not the case this time.\
    <br><br><b>3. What made you happy this week?</b>\
    <br><br>I finished a sewing project I had been putting off while school was in session, and gave them to my boyfriend! I used what I thought was a really cute teal fabric with white stars, but all he had to say about it was that it looked patriotic. Oh well. I also bought 7 pairs of earrings in the last 2 days. I haven’t worn earrings in years, but everyone has them on TikTok and I felt inspired to start wearing them.\
    <br><br><b>4. What's your pick-of-the-week or tip-of-the-week?</b>\
    <br><br>My tip-of-the-week is to check your Xbox One before buying physical games. My edition doesn’t have a disk drive, which I didn’t realize, and I wasted $40 on Amazon when I should have just bought digital."
)
try:
    session.query(BlogPost).filter_by(title=new_post.title).one()
except:
    session.add(new_post)
    session.commit()

generate_html()

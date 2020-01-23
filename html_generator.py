from database_setup import Base, BlogPost
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import path

engine = create_engine('sqlite:///blog_posts.db')
Base.metadata.bind = engine

def generate_html():
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    posts = session.query(BlogPost)

    for post in posts:
        post_title_url = post.title.replace(' ', '-')
        post_path = 'templates/posts/' + post.date + post_title_url + '.html'
        if not path.exists(post_path):
            f = open(post_path, "w")
            f.write("<!doctype html>\n<html>\n\t<head>\n\t\t<meta charset='utf-8'>\n\t\t<title>" + post.title + "</title>\n\t\t<link rel='stylesheet' href='../../static/style.css'>\n\t\t<link href='https://fonts.googleapis.com/css?family=Grand+Hotel|Sacramento|Cabin&display=swap' rel='stylesheet'>\n\t\t<script src='https://kit.fontawesome.com/4f57decedc.js' crossorigin='anonymous'></script>\n\t</head>\n\t<body>\n\t\t<header>\n\t\t\t<img class='me' src='/static/me.png'>\n\t\t\t<div id='banner'>\n\t\t\t\t<a href='/../#about-me'>About</a>\n\t\t\t\t<a href='/../#experience-header'>Experience</a>\n\t\t\t\t<a href='/../#projects-header'>Projects</a>\n\t\t\t\t<a href='/blog'>Blog</a>\n\t\t\t</div>\n\t\t</header>\n\t\t<div id='post-header'>\n\t\t\t<img class='cloud right-cloud' src='/static/cloud.svg'>\n\t\t</div>\n\t\t<div id=post>\n\t\t\t<h1>" + post.title + "</h1>\n\t\t\t<h2>" + post.date + "</h2>\n\t\t\t<p>" + post.content + "</p>\n\t\t</div>\n\t\t<footer class='container'>\n\t\t\t<div class='row'>\n\t\t\t\t<a class='item-left' href='/static/resume.pdf' download='resume-rfortanely'>resumé</a>\n\t\t\t\t<a class='item-right' href='http://github.com/codesmary'>github</a>\n\t\t\t</div>\n\t\t\t<div class='row'>\n\t\t\t\t<a class='item-left' href='https://www.linkedin.com/in/rosemary-fortanely/'>linkedin</a>\n\t\t\t\t<a class='item-right' href='mailto:elizabeth.fortanely@gmail.com'>hire me</a>\n\t\t\t</div>\n\t\t\t<p> Made with <i class='fas fa-heart'></i> by Rosemary Fortanely</p>\n\t\t</footer>\n\t</body>\n</html>")
            f.close()

generate_html()
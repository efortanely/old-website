from flask import Flask, render_template, url_for
from database_setup import Base, BlogPost
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///blog_posts.db')
Base.metadata.bind = engine

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog.html')
def blog():
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    posts = [post for post in session.query(BlogPost)]
    posts.sort(key=lambda post: datetime.strptime(post.date, '%m-%d-%Y'), reverse=True)
    return render_template('blog.html', posts=posts)

@app.route('/blog/<string:post_date>' + '<string:post_title>.html')
def blogPost(post_date, post_title):
    return render_template('posts/' + post_date + post_title + '.html')
    

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

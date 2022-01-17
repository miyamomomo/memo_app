from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


db_uri = 'mysql+pymysql://root:@localhost/memo?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text())
    content = db.Column(db.Text())


@app.route('/')
def list():

    message = 'Hello paiza memo'
    posts = Post.query.all()

    return render_template('list.html', message = message, posts = posts)

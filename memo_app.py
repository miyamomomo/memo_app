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

#メモアプリ表示
@app.route('/')
def list():

    message = 'memo'
    posts = Post.query.all()

    return render_template('list.html', message = message, posts = posts)

#詳細メモ表示
@app.route('/show/<int:id>')
def show_post(id):

    message = 'Your memo ' + str(id)
    post = Post.query.get(id)

    return render_template('show.html', message = message, post = post)

#新規メモ
@app.route('/new')
def new_post():

    message = 'New memo'
    return render_template('new.html', message = message)

#新規メモ作成
@app.route('/create', methods=['POST'])
def create_post():

    message = 'create your memo'

    new_post = Post()
    new_post.title = request.form['title']
    new_post.content = request.form['content']
    db.session.add(new_post)
    db.session.commit()

    post = Post.query.get(new_post.id)

    return render_template('show.html', message = message, post = post)

#メモ削除
@app.route('/destroy/<int:id>')
def destroy_post(id):

    message = 'delete memo ' + str(id)

    destroy_post = Post.query.get(id)
    db.session.delete(destroy_post)
    db.session.commit()

    posts = Post.query.all()

    return render_template('list.html', message = message, posts = posts)
#メモ編集画面
@app.route('/edit/<int:id>')
def edit_post(id):

    message = 'Edit memo'+str(id)
    post=Post.query.get(id)
    return render_template('edit.html', message = message,post=post)
#メモ編集
@app.route('/update/<int:id>', methods=['POST'])
def update_post(id):

    message = 'update your memo'

    post = Post.query.get(id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.commit()

    return render_template('show.html', message = message, post = post)

from flask import Flask, request, redirect, render_template
from Flask_SQLAlchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lol@localhost:8889/build-a-blog'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


#form =''' 
#<!doctype html>
#<html>
#    <body>
#        <form action="/blog" method="post">
#            <label for="blog">Blog:</label>
#            <input id="blog" type="text" name="blog" />
#            <input type="submit" />
#        </form>
#    </body>
#</html>
#'''

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog')
def blog():
    blog_id = request.args.get('id')

    if blog_id == None:
        posts = Blog.query.all()
        return render_template('blog.html', posts=posts, title='Build-a-blog')
    else:
        post = Blog.query.get(blog_id)
        return render_template('entry.html', post=post, title='Blog Entry')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        blog_title = request.form['blog-title']
        blog_body = request.form['blog-entry']
       

    return render_template('newpost.html', title='New Entry')


if  __name__ == "__main__":
    app.run(debug=True)


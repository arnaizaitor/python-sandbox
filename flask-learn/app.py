import sys

from flask import Flask
from flask import render_template
#PyMongo
from flask_pymongo import PyMongo
# PageResult 
from frontend.templates.PageResult import PageResult 
# BDD
from data.data import posts, post_body

app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')
# DB config
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskMongoDB"
mongo = PyMongo(app, connect=True)

#try
'''
i = 0
for post in posts:
    mongo.db.posts.insert({
        "id" : i,
        "title" : post,
        "content" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."
    })
    i = i+1
'''
posts_mdb = list(mongo.db.posts.find({}))
postList = [post['title'] for post in posts_mdb]


#############################   R O U T I N G   #############################
@app.route('/')
@app.route('/posts')
@app.route('/posts/<int:pagenum>')
def home(pagenum = 0):
    print(list(postList), file=sys.stderr)
    return render_template("index.html", posts = PageResult(postList, pagenum))  

@app.route('/post/<string:slug>/')
def show_post_slug(slug):
    return render_template("post_view.html", slug_title = slug, post_body = post_body)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

if __name__ == "__main__":
    app.run()
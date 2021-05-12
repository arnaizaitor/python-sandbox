import sys

from flask import Flask
from flask import render_template
#PyMongo
from flask_pymongo import PyMongo
# PageResult 
from frontend.templates.PageResult import PageResult 

app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')
# DB config
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskMongoDB"
mongo = PyMongo(app, connect=True)

#############################   R O U T I N G   #############################
@app.route('/')
@app.route('/posts')
@app.route('/posts/<int:pagenum>')
def home(pagenum = 0):
    postList = [post['title'] for post in list(mongo.db.posts.find({}))]
    return render_template("index.html", posts = PageResult(postList, pagenum))  

@app.route('/post/<string:title>/')
def show_post_content(title):
    post_body = mongo.db.posts.find_one({"title":"Lorem ipsum dolor sit amet"})['content']
    return render_template("post_view.html", post_title = title, post_body = post_body)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

if __name__ == "__main__":
    app.run()
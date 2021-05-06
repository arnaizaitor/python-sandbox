from flask import Flask
from flask import render_template

from data.data import posts

app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')

#############################   R O U T I N G   #############################
@app.route('/')
def home():
    return render_template("index.html", posts=posts)  

@app.route('/post/<string:slug>/')
def show_post_slug(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

if __name__ == "__main__":
    app.run()
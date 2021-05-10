from flask import Flask
from flask import render_template

from data.data import posts

app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')

class PageResult:
   def __init__(self, data, page = 0, posts_per_page = 32):
    self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, posts_per_page]))
    self.posts = data[page*posts_per_page:(page+1)*posts_per_page]
    self.isLastPage = False
    if(len(self.posts) < posts_per_page):
        self.isLastPage = True
    self.isVoidNextPage = False
    if(len(data[(page+1)*posts_per_page:(page+2)*posts_per_page]) == 0):
        self.isVoidNextPage = True
    
   def __iter__(self):
     for i in self.posts:
       yield i

def getPostsInPage(data, pagenum, posts_per_page):
    return data[pagenum*posts_per_page:(pagenum+1)*posts_per_page]


#############################   R O U T I N G   #############################
@app.route('/')
@app.route('/<int:pagenum>')
def home(pagenum = 0):
    return render_template("index.html", posts = PageResult(posts, pagenum))  

@app.route('/post/<string:slug>/')
def show_post_slug(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

if __name__ == "__main__":
    app.run()
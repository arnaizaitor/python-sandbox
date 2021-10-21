class PageResult:
   def __init__(self, data, page = 0, posts_per_page = 33):
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
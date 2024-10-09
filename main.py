from fastapi import FastAPI, Body

app = FastAPI()

"""
    For Learning purpose I am using local storage for the fetching the data, in my apis
"""

Blogs = [
    {"id": 1, "title": "blog", "content": "This is the content of Blog 1", "author": "Author 1", "category": "math"},
    {"id": 2, "title": "Blog 2", "content": "This is the content of Blog 2", "author": "Author 2", "category": "math"},
    {"id": 3, "title": "Blog 3", "content": "This is the content of Blog 3", "author": "Author 3",
     "category": "history"},
    {"id": 4, "title": "Blog 4", "content": "This is the content of Blog 4", "author": "Author 4",
     "category": "history"},
    {"id": 5, "title": "Blog 5", "content": "This is the content of Blog 5", "author": "Author 1",
     "category": "science"},
]


@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/blogs")
async def get_all_blogs():
    return Blogs

@app.get("/blogs/{blog_title: str}")
async def get_blog_by_title(blog_title: str):
    print(blog_title)
    for blog in Blogs:
        if blog.get('title').casefold() == blog_title.casefold():
            return blog
    return {"message": "Blog with title: {} not found".format(blog_title)}

@app.get("/blogs/")
async def get_blog_by_author(blog_author: str):
    blogs = []
    for blog in Blogs:
        if blog.get('author').casefold() == blog_author.casefold():
            blogs.append(blog)
    if len(blogs) > 0:
        return blogs
    return {"message": "Blog with author: {} not found".format(blog_author)}

@app.get("/blogs/{blog_id: int}")
async def get_blog_by_id(blog_id: int):
    for blog in Blogs:
        if blog.get('id') == blog_id:
            return blog
    return {"message": "Blog with id: {} not found".format(blog_id)}

@app.post("/blogs/create_blog")
async def create_blog(blog=Body(...)):
    Blogs.append(blog)

@app.put("/blogs/{blog_id: int}")
async def update_blog(blog_id: int, updated_book=Body()):
    for i in range(len(Blogs)):
        if Blogs[i].get('id') == blog_id:
            updated_book["id"] = blog_id
            Blogs[i] = updated_book
            return {"message": "Blog with id: {} has been updated".format(blog_id)}
    return {"message": "Blog with id: {} not found".format(blog_id)}

@app.delete("/blogs/{blog_id: int}")
async def delete_blog(blog_id: int):
    for i in range(len(Blogs)):
        if Blogs[i].get('id') == blog_id:
            Blogs.pop(i)
            return {"message": "Blog with id: {} has been deleted".format(blog_id)}
    return {"message": "Blog with id: {} not found".format(blog_id)}
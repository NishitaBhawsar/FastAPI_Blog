
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "title": "Getting Started with FastAPI",
        "content": "Learn how to build REST APIs using FastAPI.",
        "author": "Nishita",
        "category": "Python",
        "published": True,
        "views": 1250
    },
    {
        "id": 2,
        "title": "Understanding REST APIs",
        "content": "REST APIs allow applications to communicate through HTTP.",
        "author": "Rahul",
        "category": "Backend",
        "published": True,
        "views": 850
    },
    {
        "id": 3,
        "title": "Introduction to SQL",
        "content": "SQL is used to store, retrieve, and manage relational database data.",
        "author": "Priya",
        "category": "Database",
        "published": False,
        "views": 420
    }
]

@app.get('/', include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html")

@app.get('/api/posts')
def get_data():
    return posts

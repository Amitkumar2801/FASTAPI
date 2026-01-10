from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello world"}

@app.get("/about")
def about():
    return {"Hello My Name Is AMIT KUMAR SHARMA , iam pursuning diploma in artificial intellingence and machine leraning from Government Polytechnic Barh,Patna "}

@app.get("/contact")
def contect():
    return {"Email": "amitkumarsharma12345@gmail.com"}

@app.get("/hobby")
def hobby():
    return {"My Hobbies are Playing Cricket , Reading Books and Watching Movies"}

@app.get("/skills")
def skills():
    return {"My Skills are Python, C++, HTML, CSS, JavaScript"}
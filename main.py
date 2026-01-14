from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'patient Management system API'}

@app.get("/about")
def about():
    return {'Message': 'A Fully functional patient management system API built with FastAPI.'}
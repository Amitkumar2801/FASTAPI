from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'patient Management system API'}

@app.get("/about")
def about():
    return {'Message': 'A Fully Functional API To Manage Your Patient Records'}
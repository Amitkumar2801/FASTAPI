from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello world"}

@app.get("/about")
def about():
    return {"Hello My Name Is AMIT KUMAR SHARMA , iam pursuning diploma in artificial intellingence and machine leraning from Government Polytechnic Barh,Patna "}

@app.get("/contact")

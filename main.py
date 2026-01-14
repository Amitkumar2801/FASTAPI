from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'patient Management system API'}

@app.get("/about")
def about():
    return {"Hello My Name Is AMIT KUMAR SHARMA , iam pursuing diploma in artificial intelligence and machine learning from Government Polytechnic Barh,Patna "}
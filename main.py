from fastapi import FastAPI
app = FastAPI()

import json

def load_data9():
    with open('patient.json', 'r') as f:
       data = json.load(f)
       return data

@app.get("/")
def hello():
    return {'message': 'patient Management system API'}

@app.get("/about")
def about():
    return {'Message': 'A Fully Functional API To Manage Your Patient Records'}
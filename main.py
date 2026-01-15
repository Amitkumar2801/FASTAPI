from fastapi import FastAPI
app = FastAPI()

import json

def load_data():
    with open('patient.json', 'r') as f:
       data = json.load(f)
       return data

@app.get("/")
def hello():
    return {'message': 'patient Management system API'}

@app.get("/about")
def about():
    return {'Message': 'A Fully Functional API To Manage Your Patient Records'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def get_patient(patient_id: str):

    # load all the patient data

    data = load_data()
    if patient_id in data :
        return data[patient_id]
    return {'error': 'patient not found'}
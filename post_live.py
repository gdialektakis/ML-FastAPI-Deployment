import requests
import json

data= {
        "age": 57,
        "workclass": "Federal-gov",
        "fnlgt": 337895,
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Female",
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": "United-States"
    }
response = requests.post('https://ml-pipeline-deployment-fastapi.herokuapp.com/predict/', data=json.dumps(data))

print(response.status_code)
print(response.json())
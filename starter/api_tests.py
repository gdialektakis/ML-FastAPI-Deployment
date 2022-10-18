# -*- coding: utf-8 -*-
"""
Created on Tuesday October 18 2022

@author: George Dialektakis

A set of 3 functions defined to test the API Get/Post functionalities
"""
import json
from starlette.testclient import TestClient
from main import app

client = TestClient(app)


# A function to test the get
def test_get():
    response = client.get("/welcome")
    assert response.status_code == 200


# A function to test the post on a predicted value of Salary >50K
def test_post_1():
    input_dict = {
        "age": 25,
        "workclass": "Self-emp-not-inc",
        "fnlgt": 176756,
        "education": "HS-grad",
        "education_num": 9,
        "marital_status": "Never-married",
        "occupation": "Farming-fishing",
        "relationship": "Own-child",
        "race": "White",
        "sex": "Male",
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 35,
        "native_country": "United-States"
    }
    response = client.post("/predict", json=input_dict)
    assert response.status_code == 200
    assert json.loads(response.text)["forecast"] == "Income < 50k"


# A function to test the post on a predicted value of Salary>50K
def test_post_2():
    input_dict = {
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
    response = client.post("/predict", json=input_dict)
    assert response.status_code == 200
    assert json.loads(response.text)["forecast"] == "Income > 50k"

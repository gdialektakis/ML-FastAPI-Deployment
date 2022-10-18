# Script to train machine learning model.
import pickle

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model
import sklearn

print('The scikit-learn version is {}.'.format(sklearn.__version__))
# Add code to load in the data.
data = pd.read_csv("census.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.2)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True)

model = train_model(X_train, y_train)

# Saving the encoder and the LabelBinarizer for being used in the API later
pickle.dump(encoder, open("starter/model/encoder.pkl", 'wb'))
pickle.dump(lb, open("starter/model/label_binarizer.pkl", 'wb'))

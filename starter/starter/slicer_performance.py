# Script to Compute the performance metrics on slices of categorical features

# Add the necessary imports
import pandas as pd
from ml.data import process_data
from ml.model import inference, compute_model_metrics
import pickle

# Add code to load in the data, model and encoder
data = pd.read_csv("census.csv")
model = pickle.load(open("../model/model.sav", 'rb'))
encoder = pickle.load(open("../model/encoder.pkl", 'rb'))
lb = pickle.load(open("../model/label_binarizer.pkl", 'rb'))


def get_sliced_formance(model, data, col, encoder, lb):
    """ Computes the performance metrics when the value of a given feature is held fixed.
    Inputs
    ------
    model : trained model
        A trained model that we want test our data against
    data: pandas dataframe
        The dataframe we'll use to slice
    col : str
        The name of the column that we want to slice data based on
    encoder : sklearn.preprocessing._encoders.OneHotEncoder
        Trained sklearn OneHotEncoder.
    lb : sklearn.preprocessing._label.LabelBinarizer
        Trained sklearn LabelBinarizer.
    Returns
    -------
    None
    This function generates a txt file with the Performance metrics over each slice
    """

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

    # Get the unique values of the feature of interest
    slices = data.loc[:, col].unique()

    # Creating a txt file where we'll write our performance results
    file_object = open('{}_slice_output.txt'.format(col), 'w')
    file_object.write('Here are the performance results for the slices of {} feature'.format(col))
    file_object.write("\n")

    # Iterating over each slice and calculating the performance metrics
    for sl in slices:
        file_object.write(sl)
        file_object.write("\n")
        df = data.loc[data.loc[:, col] == sl, :]
        # Process the test data with the process_data function.
        X_test, y_test, encoder, lb = process_data(
            df, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb)
        preds = inference(model, X_test)
        precision, recall, fbeta = compute_model_metrics(y_test, preds)
        file_object.write('Precision: {} '.format(precision))
        file_object.write("\n")
        file_object.write('Recall: {} '.format(recall))
        file_object.write("\n")
        file_object.write('fbeta: {} '.format(fbeta))
        file_object.write("\n")
        file_object.write("*-*" * 5)
        file_object.write("\n")
    file_object.close()


# Let's try this function on the workclass column
if __name__ == "__main__":
    get_sliced_formance(model, data, "workclass", encoder, lb)

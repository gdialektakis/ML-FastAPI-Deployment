# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- This model is created for Project 3 of the ML DevOps Nanodegree from Udacity
- Created on 10/18/2022
- Version 1.0
- We used a Random Forest Classifier from scikit-learn in this project
- For more information about the model, please refer to Udacity Nanodegree program
## Intended Use
- This project is intended to show an example of deploying a Scalable ML Pipeline in Production using FastAPI and Heroku.
- Predict whether income exceeds $50K/yr based on census data
## Training Data
- Predict whether income exceeds $50K/yr based on census data. Also known as "Adult" dataset.
- Extraction was done by Barry Becker from the 1994 Census database.
- More information at: https://archive.ics.uci.edu/ml/datasets/census+income
- We have used 80% of the original dataset for the training purposes of the model.
## Evaluation Data
- We have used 20% of the original dataset for evaluation purposes of the model.
## Metrics
- We have used three metrics in this project; fbeta_score, precision_score and recall_score.
- Our model's performance is:
  - Fbeta_score:
  - Precision_score:
  - Recall_score:

## Ethical Considerations
- None to be aware of.
## Caveats and Recommendations
- The performance of the model can be improved using either more advanced classifiers or by implementing hyperparameter tuning.
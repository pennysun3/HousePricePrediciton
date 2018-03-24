"""
This is the main modeling file for the house price prediciton webapp.
Author: Junxiong Liu
"""

import pandas as pd
import numpy as np
import os
from scipy import stats
from scipy.stats import norm
from sklearn.ensemble import RandomForestRegressor
from sqlalchemy import create_engine
import logging
from sklearn.externals import joblib


def prediction(OverallQual, GrLivArea, GarageCars,YearBuilt,FullBath):
    """Predict house price based on user input
    Args:
        param1 (int): user input of house overall quality 1-10
        param2 (int): user input of living area in square foot
        param3 (int): user input of number of cars in garage
        param4 (int): user input of house built year
        param5 (int): user input of number of full baths
    Returns:
        result: the predicted house price
        
    """
    # Create of row of data that comabines all user inputs
    title={"OverallQual":[OverallQual], "GrLivArea":[GrLivArea], "GarageCars":[GarageCars],"YearBuilt":[YearBuilt],"FullBath":[FullBath]}
    test = pd.DataFrame(title)

    #import pickled model
    trained_model = joblib.load('model.pkl')

    # Make prediction from the loaded random forest model
    predict = trained_model.predict(test)[0]
    result="${:,.2f}".format(predict)
    return result

#print(prediction(10,200,3,2010,3))
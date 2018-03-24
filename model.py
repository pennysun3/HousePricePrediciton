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


logging.basicConfig(level=logging.DEBUG)
logging.info("begin training")

  
def pricecal():
    """Calculate house price (csv format)
    Args:
        NULL
    Returns:
        rf: the fitted random forest model
    """      
    DB_URL = 'mysql+pymysql://root:mypassword@tryrds.cfxcvwdxc0al.us-east-2.rds.amazonaws.com:3306/flask'
    engine = create_engine(DB_URL)
    train_new=pd.read_sql_query('select * from train',con=engine)
    
    features=['OverallQual',
     'GrLivArea',
     'GarageCars',
     'YearBuilt',
     'FullBath']
    
    trainset=train_new[features]
    targetset=train_new['SalePrice']
    
    
    rf = RandomForestRegressor(max_depth=3,
                  min_samples_split=10,
                  n_estimators=100,
                  max_features=5,
                  random_state=12345)
    rf= rf.fit(trainset,targetset)

    return rf

# Create pickle file
# save the model to disk
joblib.dump(pricecal(), 'model.pkl') 


logging.info("finish training")



#print(prediction(3,100,2,1980,2))

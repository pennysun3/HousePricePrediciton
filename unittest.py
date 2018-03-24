"""
This is the main modeling file for the house price prediciton webapp.
Author: Mengyu Sun
"""

import pandas as pd
import numpy as np
from predict import prediction
from sqlalchemy import create_engine
from sklearn.externals import joblib

DB_URL = 'mysql+pymysql://root:mypassword@tryrds.cfxcvwdxc0al.us-east-2.rds.amazonaws.com:3306/flask'
engine = create_engine(DB_URL)
    # Create DataFrame
df=pd.read_sql_query('select * from train',con=engine)
len(df.columns)

def test_data():
    """Test data.py for column count and data type."""
    DB_URL = 'mysql+pymysql://root:mypassword@tryrds.cfxcvwdxc0al.us-east-2.rds.amazonaws.com:3306/flask'
    engine = create_engine(DB_URL)
    # Create DataFrame
    df=pd.read_sql_query('select * from train',con=engine)
    # Check type of output
    assert isinstance(df, pd.DataFrame)
    # Check column count
    assert len(df.columns) == 81

#test_data()

def test_predict():
    """Test predict.py for array length and data type."""
    # Create a row of data and run prediction
    user1 = '10'
    user2 = '200'
    user3 = '3'
    user4 = '2010'
    user5 = '3'
    result = prediction(user1,user2,user3,user4,user5)
    
    # Check type of output
    assert isinstance(result, str)
    # Check prediction result
    assert result == "$120,384.98"

#test_predict()
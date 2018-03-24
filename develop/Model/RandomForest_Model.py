import pandas as pd
import numpy as np
import os
from scipy import stats
from scipy.stats import norm
from sklearn.ensemble import RandomForestRegressor
from sqlalchemy import create_engine

  
def pricecal():    
    #train.drop(train[train['GrLivArea'] > 4000].index, inplace=True)
    #train["GarageCars"].fillna(0, inplace=True) 
#    path=os.getcwd()
#    train=pd.read_csv(path+"/train.csv")
#    train_new = train[train['SalePrice'].notnull()]
    DB_URL = 'mysql+pymysql://root:mypassword@tryrds.cfxcvwdxc0al.us-east-2.rds.amazonaws.com:3306/flask'

    #config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    #config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

    engine = create_engine(DB_URL)

    #train.to_sql(name='train', con = engine, if_exists = 'append', index=False)
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
                  max_features=5)
    rf= rf.fit(trainset,targetset)

    return rf


def prediction(OverallQual, GrLivArea, GarageCars,YearBuilt,FullBath):
    # Create of row of data that comabines team attributes and playing styles for home and away teams
    title={"OverallQual":[OverallQual], "GrLivArea":[GrLivArea], "GarageCars":[GarageCars],"YearBuilt":[YearBuilt],"FullBath":[FullBath]}
    test = pd.DataFrame(title)

    model=pricecal()
    # Make prediction from the loaded logistic regression model
    predict = model.predict(test)[0]
    result="${:,.2f}".format(predict)
    return result

#print(prediction(3,100,2,1980,2))

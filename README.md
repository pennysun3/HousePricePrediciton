# House price estimate

* **Developer**: [Penny Sun](https://github.com/pennysun3)
* **Product Owner**: [Jill Fan](https://github.com/jill-fan)
* **QA**: [Logan Wilson](https://github.com/lwilson18)

------------
* **Vision**: 
Build a house price estimate application so that consumers can get easy access to home value information by entering a list of criteria, and build up a trusted marketplaces for real estate information in the U.S.

* **Mission**: 
Based on statistical and machine learning models that analyze large set of data points on each property. and continually improving the RMSE prediction error. This will be done using a random forest model or a XGBoost model that is trained with the [Kaggle Iowa State House Sale Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

* **SuccessCriteria**: Successfully deployed a web application that dynamically shows a house price estimate according to user input.


Suggested steps to deploy app
------------

1. Clone repository.
2. Use conda to create virtual environment

   ```
   > House-Estimate$ conda create -n houseproject python=3
   > House-Estimate$ source activate houseproject
   ```
3. Install required packages

   ```
   > (houseproject) House-Estimate$ pip install -r requirements.txt
   ```
  
4. Set up house.env file with the following structure
   
   ```
   export DATABASE_URL=XXX
   export HOST=XXX    
   export USER=XXX
   export PASSWORD=XXX
   export DBNAME=XXX    
   export PORT=XXX
   ```

5. Set environment variables from file

   ```
   source house.env
   ```

6. (OPTIONAL) If you want to run unit tests before running the code, run the following commands:

   ```
   > (houseproject) House-Estimate$ py.test
   ```

7. Download training data from [Kaggle] (https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) as train.csv.

8. Launch the application

   ```
   > (houseproject) House-Estimate$ python application.py
   ```


   

Application Screenshot
------------

![](https://github.com/pennysun3/HousePricePrediction/blob/master/screenshots/page1.jpg)
![](https://github.com/pennysun3/HousePricePrediction/blob/master/screenshots/page2.jpg)

PivotalTracker
------------
For this project, we used Pivotal Tracker, an Agile Project Management Software, to keep track of the overall progress. The pivotal tracker page for this project can be reached by clicking on [this link](https://www.pivotaltracker.com/n/projects/2142050).


Documentation
------------
* `EDA`: Jupyter Notebook that contains a walkthrough of the EDA. [[jupyter notebook](https://github.com/pennysun3/HousePricePrediction/blob/master/develop/EDA/House_EDA.ipynb)]

* `Random Forest Model`: A walkthrough of the overall random model building process. [[jupyter notebook](https://github.com/pennysun3/HousePricePrediction/blob/master/develop/Model/RandomForest_Model.py)]

* `XGBoost Model`: An old version of the overall model building process. [[jupyter notebook](https://github.com/pennysun3/HousePricePrediction/blob/master/develop/Model/House_XGBoost_Model.ipynb)]

* Step by step guide for database, environment and sphinx documentation set up. [[Github Wiki](https://github.com/pennysun3/HousePricePrediction/wiki)]

* You can find the slides for this project [here](https://github.com/pennysun3/HousePricePrediction/blob/master/House_Presentation.pdf).
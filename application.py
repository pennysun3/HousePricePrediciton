from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from model import prediction


# needed by beanstalk
application = Flask(__name__)

# config
application.config.from_object(__name__)

@application.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')
 
# show the model
@application.route('/',methods=['POST'])
def print():
    user1 = request.form['OverallQual']
    user2 = request.form['GrLivArea']
    user3 = request.form['GarageCars']
    user4 = request.form['YearBuilt']
    user5 = request.form['FullBath']

    housepred= prediction(user1,user2,user3,user4,user5)
    return render_template('result.html', result=housepred)
   
if __name__ == "__main__":
    application.run()
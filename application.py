"""

This is the flask application page for the house prediction webapp.

Author: Mengyu Sun

"""
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
import logging
from predict import prediction

# needed by beanstalk
application = Flask(__name__)

# config
application.config.from_object(__name__)

@application.route('/', methods=['GET'])
def mainpage():
    """Main page of the webapp

    Args:
        Null

    Returns:
        flask-obj: rendered html page
        
    """
    # logging
    logger.info('Going to main page.')
    return render_template('index.html')
 
@application.route('/',methods=['POST'])
def print():
    """Result page of webapp

    Args:
        Null

    Returns:
        flask-obj: rendered html page

    """
    user1 = request.form['OverallQual']
    user2 = request.form['GrLivArea']
    user3 = request.form['GarageCars']
    user4 = request.form['YearBuilt']
    user5 = request.form['FullBath']

    # logging
    #logger.info('Got user input.')

    # predict house price using model.prediction
    housepred= prediction(user1,user2,user3,user4,user5)

    # logging
    logger.info('Successfully predict price for user input.')
    return render_template('result.html', result=housepred)
   
if __name__ == "__main__":
    # logger initialization
    logging.basicConfig(filename='application.log', level=logging.DEBUG)
    logger = logging.getLogger(__name__) 
    application.run(host = '0.0.0.0', use_reloader=True, debug=True)
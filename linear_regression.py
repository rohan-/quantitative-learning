# -*- coding: utf-8 -*-
"""
Implementation largely adapted from Quantopian
"""

import numpy as np
import pandas.io.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels import regression
import datetime

def getData(ticker):
    startDate = datetime.datetime(2014, 1, 1)
    endDate = datetime.datetime(2015, 1, 1)
    
    return __getReturns(web.DataReader(str(ticker), 'yahoo', startDate, endDate)
                                                            ['Adj Close'].values)
                                                            
def __getReturns(asset):
    return asset[1:] / asset[:-1] - 1
                                                            
def linearRegression(X, Y):
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()

    alpha = model.params[0]
    beta = model.params[1]
    X = X[:,1]
    
    print "alpha:", alpha
    print "beta:", beta
    
    X2 = np.linspace(X.min(), X.max(), 100)
    Y_hat = X2 * beta + alpha
    
    plt.scatter(X, Y, alpha = 0.3)
    plt.plot(X2, Y_hat, 'r', alpha = 0.9)
    plt.xlabel('S&P500 Daily Returns')
    plt.ylabel('Asset Daily Returns')
    
    return model.summary()

print(linearRegression(getData('^GSPC'), getData('AAPL')))

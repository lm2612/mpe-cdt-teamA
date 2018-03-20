import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import read_data as rd

# choose which data sets to use
loss_data_name = '../AIR_data/Correct_loss_data/Region_1_DR.csv'
predictor_name = 'GEM_HistoricalFreq.csv'

LOB = 'LOB1'
predictor = 'SUM_FREQ'

# import data sets
loss_data = rd.getLOBdata(loss_data_name)
predictor_data = rd.predictor(predictor_name)

# separate into data for training and testing
train_loss_data, test_loss_data = rd.take_out_test(loss_data)
train_pred_data, test_pred_data = rd.take_out_test(predictor_data)

# clean data to use only shared airsids
correlation = rd.clean_data(train_loss_data, train_pred_data, LOB, predictor)
correlation_test = rd.clean_data(test_loss_data, test_pred_data, LOB, predictor)

# do regression analysis
model = ols(str(LOB)+' ~ '+str(predictor), correlation).fit()

# make linear relationship
X = np.linspace(min(correlation[predictor]), max(correlation[predictor]), 100)
fitted_model = model._results.params[0] + X*model._results.params[1]

print(model._results.params)
plt.close()
plt.plot(correlation[predictor], correlation[LOB], marker='+', linestyle='')
plt.plot(correlation_test[predictor], correlation_test[LOB], marker='+', linestyle='', color='red')
plt.plot(X, fitted_model)
plt.show()

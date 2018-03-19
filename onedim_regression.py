# A one-dimensional regression of a Predictor (here Global Historical Frequency)
# and a region of AALs (in this case Region One).
# WARNING: the fit is shit.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats import kurtosistest
from statsmodels.formula.api import ols

print(pd.__version__)

# Load csv ad a datafarme object using pandas
Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')
Historial_freq = pd.read_csv('../AIR_data/Predictor_Data/GEM_HistoricalFreq.csv')

Region_1_DR = pd.DataFrame(Region_1_DR)
Region_1_DR = Region_1_DR.sort(['AIRSID'])

# Select unique location ID in the AIRSID column
unique_arsid=Region_1_DR.AIRSID.unique()

aal = np.zeros((len(unique_arsid), 2))
freq = Historial_freq.loc[Historial_freq['AIRSID'].isin(unique_arsid)]

for i in range(0, len(unique_arsid)) :
	# For each unique AIRSID find the sum of LOB1
	aal[i, 0] = unique_arsid[i]
	aal[i, 1] = Region_1_DR.loc[Region_1_DR['AIRSID'] == unique_arsid[i], 'LOB1' ].sum()
	#freq[i] = Historial_freq.loc[Historial_freq['AIRSID']==unique_arsid[i]]
	
#  Historial frequencies is missing AIRSIDs 10655 and 10656 so remove 
aal = np.delete(aal, (1,2), axis=0)


data = pd.DataFrame({'x': freq['SUM_FREQ'], 'y': aal[:,1]})

#Fit the model
model = ols("y ~ x", data).fit()

X = np.linspace(min(freq['SUM_FREQ']), max(freq['SUM_FREQ']), 100)
fitted_model = model._results.params[0] + X*model._results.params[1]

# Print the summary
print(model.summary())

print("\nRetrieving manually the parameter estimates:")
print(model._results.params)

plt.scatter(freq['SUM_FREQ'], aal[:,1])
plt.plot(X, fitted_model)
plt.show()

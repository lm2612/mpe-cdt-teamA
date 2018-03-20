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
# IMPORTANT: THIS USES ALL THE DATA -- NEED TO ADD STRIPPING FOR TESTING
Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')
GDP = pd.read_csv('../AIR_data/Predictor_Data/Global475yrPGA.csv')

Region_1_DR = pd.DataFrame(Region_1_DR)
Region_1_DR = Region_1_DR.sort(['AIRSID'])

# Select unique location ID in the AIRSID column
unique_arsid=Region_1_DR.AIRSID.unique()

aal = np.zeros((len(unique_arsid), 2))
freq = GDP.loc[GDP['AIRSID'].isin(unique_arsid)]

for i in range(0, len(unique_arsid)) :
	# For each unique AIRSID find the sum of LOB1
	aal[i, 0] = unique_arsid[i]
	aal[i, 1] = Region_1_DR.loc[Region_1_DR['AIRSID'] == unique_arsid[i], 'LOB1' ].sum()

print(np.count_nonzero(aal))
print(np.count_nonzero(freq))


#take logs for better fit  -- CHECK FOR NON-ZEROS
#aal = np.log(aal)
#freq = np.log(freq)

data = pd.DataFrame({'x': freq['AVERAGE_PGA_475yr'], 'y': aal[:,1]})

fig, ax = plt.subplots()
#ax.plot(x2, y2, color='r', label='Fit. func: $f(x) = %.3f e^{%.3f x} %+.3f$' % (a,k,b))
ax.plot(freq['AVERAGE_PGA_475yr'], aal[:,1], 'bo', label='data with noise')
ax.legend(loc='best')
plt.show()

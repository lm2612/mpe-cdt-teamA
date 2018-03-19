import math
import pandas as pd
import numpy as np
from read_data import *

regiondata = getLOBdata('../AIR_data/Correct_loss_data/Region_1_DR.csv')
regiondata = regiondata.sort_values('AIRSID')


inputdata = predictor('GEM_HistoricalFreq.csv')

inputname = list(inputdata)[1]

# Add column to region data
regiondata[inputname] = pd.Series() 

for AIR_ID in inputdata['AIRSID']:
	if AIR_ID in list(regiondata['AIRSID']):
		# Add inputdata[inputname] to regiondata[inputname]
		regiondata[inputname] = inputdata[inputname]

		
print(regiondata)

import matplotlib.pyplot as plt

plt.plot(regiondata[inputname],regiondata['LOB1'],'ko')
plt.show()

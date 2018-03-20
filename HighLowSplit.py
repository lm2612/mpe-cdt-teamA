import math
import pandas as pd
import numpy as np
from read_data import * 
import matplotlib.pyplot as plt


def AddDum(allregions):
    """ Splits into high and low hazards for data frame allregions"""
    # create data
    allreg_plusdum= allregions.copy()
    Select_names = ['SUM_NIGHTLIGHTS','AVERAGE_PGA_475yr','TOTAL_POP']
    Dummy_names = ['SUM_NIGHTLIGHTS_DUM','AVERAGE_PGA_475yr_DUM','TOTAL_POP_DUM']
    

    
    for name in Dummy_names:
        allreg_plusdum[name]= np.arange(len(allregions['AIRSID']))
    
     
    for col in Select_names:
        values = allregions[col]
        mean = np.mean(values)
        print(col , mean)
        
        for index, row in allregions.iterrows():
            if values[index] >= mean:
                allreg_plusdum[col+'_DUM'].loc[index] = 1.0
                
            else:
                
                allreg_plusdum[col+'_DUM'].loc[index] = 0.0
    
    
    return( allreg_plusdum)
    
    




def get_all_regions():
	""" Concatenates alldataframes from get_data_for_region """
	region_dataframes = []
	for i in range(1,9):
		region_dataframes.append(get_data_for_region(i))

	allregions = pd.concat(region_dataframes)

	return allregions

allregions = get_all_regions()
highhazard,lowhazard = High_Low_Split(allregions)

print( highhazard)


plt.plot(highhazard['AIRSID'],highhazard['AVERAGE_PGA_475yr'],'ro')
plt.plot(lowhazard['AIRSID'],lowhazard['AVERAGE_PGA_475yr'],'ko')

plt.show()

plt.clf()
plt.plot(allregions['AIRSID'],allregions['AVERAGE_PGA_475yr'],'ko')
plt.show()




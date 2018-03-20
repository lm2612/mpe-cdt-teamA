import math
import pandas as pd
import numpy as np
from read_data import * 
import matplotlib.pyplot as plt

def High_Low_Split(allregions):
	""" Splits into high and low hazards for data frame allregions"""
	# create data
        high = pd.DataFrame(columns=allregions.columns)
        low = pd.DataFrame(columns=allregions.columns)


        pgas = allregions['AVERAGE_PGA_475yr']
	mean_pga = np.mean(pgas)
	print(mean_pga)
        for index, row in allregions.iterrows():
                if pgas[index] >= mean_pga:
                        high.loc[index] = row
                else:
                        low.loc[index] = row

        return high,low


def get_all_regions():
	""" Concatenates alldataframes from get_data_for_region """
	region_dataframes = []
	for i in range(1,9):
		region_dataframes.append(get_data_for_region(i))

	allregions = pd.concat(region_dataframes)

	return allregions

allregions = get_all_regions()
highhazard,lowhazard = High_Low_Split(allregions)

print highhazard


plt.plot(highhazard['AIRSID'],highhazard['AVERAGE_PGA_475yr'],'ro')
plt.plot(lowhazard['AIRSID'],lowhazard['AVERAGE_PGA_475yr'],'ko')

plt.show()

plt.clf()
plt.plot(allregions['AIRSID'],allregions['AVERAGE_PGA_475yr'],'ko')
plt.show()

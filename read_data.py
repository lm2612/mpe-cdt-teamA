import pandas as pd
import math
import numpy as np

# # Load csv ad a datafarme object using pandas
# Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')
# print(list(Region_1_DR))

# # Select unique location ID in the AIRSID column
# unique_arsid=Region_1_DR.AIRSID.unique()
# for air_id in unique_arsid :
# 	# For each unique AIRSID finr the mean of LOB1
# 	print(air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB4' ].sum())
		
def getLOBdata(csvname):
	region_data=pd.read_csv(csvname)
	headernames = list(region_data)
	lobnames = headernames[3:3+6]
	unique_arsid=region_data['AIRSID'].unique() # change to region_data.headernames[0] to make more flexible
	data_output = np.zeros([len(unique_arsid), len(lobnames)+1])
	data_output.fill(np.nan)
	print(data_output.shape)

	for j, lob in enumerate(lobnames):
		for i, air_id in enumerate(unique_arsid):
			data_output[i, 0] = air_id 
			lobsum = region_data.loc[region_data['AIRSID']==air_id, lob  ].sum()
			if math.isnan(lobsum)=='True':
				print('No data for ',lobsum, ', skipping this data')
			else:
				data_output[i, j+1] = lobsum


	# i=1
	# for lob in lobnames:
	# 	print(lob)
	# 	j=0
	# 	for air_id in unique_arsid:
	# 		data_output[j, 0] = air_id 
	# 		lobsum = region_data.loc[region_data['AIRSID']==air_id, lob  ].sum()
	# 		if math.isnan(lobsum)=='True':
	# 			print('No data for ',lobsum, ', skipping this data')
	# 		else:
	# 			data_output[j, i] = lobsum
	# 		j+=1
	# 	i +=1
	print(data_output)

getLOBdata('../AIR_data/Correct_loss_data/Region_1_DR.csv')
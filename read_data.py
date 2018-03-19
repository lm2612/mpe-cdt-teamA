import pandas as pd

# Load csv ad a datafarme object using pandas
Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')

# Select unique location ID in the AIRSID column
unique_arsid=Region_1_DR.AIRSID.unique()
for air_id in unique_arsid :
	# For each unique AIRSID finr the mean of LOB1
	print(air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB1' ].mean())
		


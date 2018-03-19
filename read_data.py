import math
import pandas as pd
import numpy as np

def getLOBdata(csvname):
	# Load csv ad a dataframe object using pandas
	region_data=pd.read_csv(csvname)
	# Get all of the headings from the csv
	headernames = list(region_data)
	# Get the names of all of the LOB columns, eg LOB1, LOB2 etc
	lobnames = headernames[3:3+6]
	# Select unique location ID in the AIRSID colum
	unique_arsid=region_data['AIRSID'].unique() # change to region_data.headernames[0] to make more flexible
	# Initialise empty nan 2d array, 1 column airsid, following columns are the LOBS
	data_output = np.zeros([len(unique_arsid), len(lobnames)+1])
	data_output.fill(np.nan)
	delete_list = [] # prep list for empty columns to delete

	for j, lob in enumerate(lobnames):
		for i, air_id in enumerate(unique_arsid):
			# Populate data_ouput with the AIRSID and the sum of each LOB
			data_output[i, 0] = air_id 
			lobsum = region_data.loc[region_data['AIRSID']==air_id, lob  ].sum()
			data_output[i, j+1] = lobsum
		# If a column has no LOB data, save the index to delete it
		if math.isnan(data_output[0, j+1]):
			delete_list.append(j+1)			

	# If a column has no LOB data, delete it
	data_output = np.delete(data_output, delete_list, axis=1)
	# Delete the names of columns not included for the dataframe
	column_names = ['AIRSID']+lobnames
	
	column_names = np.delete(column_names, delete_list, axis=1)
	df_output = pd.DataFrame(data_output, columns=column_names)

	return df_output


def predictor(name):
        """
        Function to read in csv file and return data frame
        """

        data = pd.read_csv('../AIR_data/Predictor_Data/'+name)
        return data


def take_out_test(data):
        """
        Function to separate a raw data frame into
        two data sets: one to train on (80% of data),
        one to test on (20% of data).

        These are pseudo-randomly decided; but
        should be the same for all airsids.
        """

        # create data
        train = pd.DataFrame(columns=data.columns)
        test = pd.DataFrame(columns=data.columns)

        # initialise indices
        test_index = 0
        train_index = 0

        airsid_index = data.columns.get_loc('AIRSID')

        # loop over rows in data
        for index, row in data.iterrows():
                # seed random number based on airsid
                np.random.seed(row[airsid_index])

                if np.random.random() > 0.8:
                        test.loc[test_index] = row
                        test_index += 1
                else:
                        train.loc[train_index] = row
                        train_index += 1

        return train, test


import pandas as pd
import numpy as np

# Load csv ad a datafarme object using pandas
Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')

# Select unique location ID in the AIRSID column
unique_arsid=Region_1_DR.AIRSID.unique()
#for air_id in unique_arsid :
	# For each unique AIRSID finr the mean of LOB1
#	print(air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB1' ].mean())

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

predict = predictor('Global_NightLights.csv')
train, test = take_out_test(predict)
print(test.values.shape, train.values.shape)

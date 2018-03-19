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

        data = pd.read_csv('../AIR_data/Predictor_Data/'+name)
        return data


def take_out_test(data):

        train = pd.DataFrame(columns=data.columns)
        test = pd.DataFrame(columns=data.columns)

        test_index = 0
        train_index = 0

        for index, row in data.iterrows():
                np.random.seed(row[0])

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

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
            #late data_ouput with the AIRSID and the sum of each LOB
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
    column_names = np.delete(column_names, delete_list, axis=0)
    #print(column_names)
    df_output = pd.DataFrame(data_output, columns=column_names)
    
    return df_output



def predictor(name):
        """
        Function to read in csv file and return data frame

        arg: name: string with name of predictor data file.
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

    arg: data: any data set in the form of a dataframe.
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
        np.random.seed(int(row[airsid_index]))
        
        if np.random.random() > 0.8:
            test.loc[test_index] = row
            test_index += 1
        else:
            train.loc[train_index] = row
            train_index += 1
                
    return train, test



def clean_data(loss_data, predictor_data, LOB, predictor):
    """
    A function that takes two data frames and returns a data frame combining 
    loss and predictor data, taking into account that some IDs might be missing.

    arg: loss_data: a dataframe with the loss data.
    arg: predictor_data: a dataframe with the predictor datas.
    arg: LOB: a string denoting which loss to look at.
    arg: predictor: the string which is the title of the predictor data.
    """
    
    # now find shared set of unique airsids
    predictor_data_airsid = predictor_data['AIRSID']
    new_unique = predictor_data.loc[predictor_data_airsid.isin(loss_data['AIRSID'])]

    print(loss_data)
    print(new_unique)
    
    # find index of columns for parameters we want
    airsid_index = new_unique.columns.get_loc('AIRSID')
    loss_index = loss_data.columns.get_loc(LOB)
    predictor_index = new_unique.columns.get_loc(predictor)
    airsid_index_1 = loss_data.columns.get_loc('AIRSID')

    # make empty data frame
    final_data = pd.DataFrame(columns=['AIRSID', predictor, LOB])
    
    # loop through rows of both data sets
    for index, row in new_unique.iterrows():
        for index1, row1 in loss_data.iterrows():
            
            # if we have matching airsid, add to new data frame
            if row[airsid_index] == row1[airsid_index_1]:
                final_data.loc[index] = [row[airsid_index], row[predictor_index], row1[loss_index]]            
        
    return final_data


def combine_clean_data(loss_data, predictor_datas, LOB, predictors):
    """
    Take some loss datas and a list of predictors, and return a dataframe of
    the common set of regions, with the corresponding losses and predictors.

    arg: loss_data: a dataframe with the loss data.
    arg: predictor_datas: a list of dataframes, with the predictor datas.
    arg: LOB: a string denoting which loss to look at.
    arg: predictors: a list of strings with corresponding to the titles of the predictors.
    """    

    # find all the common airsids for the predictor data that we're interested in
    shared_airsids = loss_data['AIRSID']
    for predictor_data in predictor_datas:
        shared_airsids = predictor_data.loc[predictor_data['AIRSID'].isin(shared_airsids)]['AIRSID']

    # make new data frame to put things in
    columns = ['AIRSID', 'LOB']
    for predictor in predictors:
        columns.append(predictor)
    final_data = pd.DataFrame(columns=columns)

    # now loop through the shared airsids to find data corresponding to it
    for index, airsid in shared_airsids.iteritems():
        row = []
        row.append(airsid)

        # find loss corresponding to this airsid and add to row
        loss = loss_data.loc[loss_data['AIRSID'] == airsid][LOB].item()
        row.append(loss)
        for predictor_data, predictor in zip(predictor_datas, predictors):
            # find predictor corresponding to this airsid and add to row
            p_value = predictor_data.loc[predictor_data['AIRSID'] == airsid][predictor].item()
            row.append(p_value)
        # add row to final data
        final_data.loc[index] = row

    return final_data
    
    
    
    
    

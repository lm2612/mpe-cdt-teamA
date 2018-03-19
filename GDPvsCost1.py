#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:39:30 2018

@author: ms5717
"""

import read_data as rd

loss_data=rd.getLOBdata('../AIR_data/Correct_loss_data/Region_1_DR.csv')

gdp_data=rd.predictor('GlobalGDP_Stats.csv')



unique_AIRSID=loss_data.AIRSID.unique()

gdp_data_airsid=gdp_data['AIRSID']

new_unique=gdp_data.loc[gdp_data_airsid.isin(loss_data['AIRSID'])]

airsid_index = new_unique.columns.get_loc('AIRSID')
loss_index = loss_data.columns.get_loc('LOB1')
gdp_index = new_unique.columns.get_loc('TOTAL_GDP')

airsid_index_1=loss_data.columns.get_loc('AIRSID')


final_data=pd.DataFrame(columns=('TOTAL_GDP','LOB1'))

for index, row in new_unique.iterrows():
    for index1, row1 in loss_data.iterrows():
        if row[airsid_index] == row1[airsid_index_1]:
            final_data.loc[index]=[row[gdp_index],row1[loss_index]]
print(final_data)
            
            
#    gdp_final.loc[index]=gdp_data.loc[gdp_data['AIRSID']==row[airsid_index],'TOTAL_GDP']
#    loss_final.loc[index]=loss_data.loc[loss_data['AIRSID']==row[airsid_index],'LOB1']
#print(gdp_final, loss_final)

#df=[gdp_final,loss_final]



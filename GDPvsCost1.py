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

new_unique=gdp_data.loc[gdp_data_airsid.isin(unique_AIRSID)]

airsid_index = new_unique.columns.get_loc('AIRSID')
print(new_unique)

for index, row in new_unique.iterrows():
    if 
#    gdp_final.loc[index]=gdp_data.loc[gdp_data['AIRSID']==row[airsid_index],'TOTAL_GDP']
#    loss_final.loc[index]=loss_data.loc[loss_data['AIRSID']==row[airsid_index],'LOB1']
#print(gdp_final, loss_final)

#df=[gdp_final,loss_final]



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import read_data as rd

# choose which data sets to use
loss_data_name = '../AIR_data/Correct_loss_data/Region_1_DR.csv'
predictor_names = ['GEM_HistoricalFreq.csv', 'Global475yrPGA.csv',
                   'GlobalAverageSoil.csv', 'GlobalGDP_Stats.csv',
                   'GlobalMIPC_Stats.csv', 'Global_NightLights.csv',
                   'GlobalPopCounts.csv', 'GlobalSeismicBudget.csv',
                   'USGS_HistoricalFreq.csv']

LOB = 'LOB1'
predictors = ['SUM_FREQ', 'AVERAGE_PGA_475yr',
              'AVERAGE_SOIL', 'TOTAL_GDP',
              'MEAN_MIPC', 'SUM_NIGHTLIGHTS',
              'TOTAL_POP', 'SUM_SEISMIC_BUDGET',
              'USGS_HISTORICAL_FREQ']

# import data sets
loss_data = rd.getLOBdata(loss_data_name)

#predictor_datas = []
#for predictor_name in predictor_names
predictor_datas = [rd.predictor(predictor_name) for predictor_name in predictor_names]

# clean data to use only shared airsids
correlation = rd.combine_clean_data(loss_data, predictor_datas, LOB, predictors)

print(correlation)

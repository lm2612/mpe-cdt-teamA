#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:35:14 2018

@author: bsa10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import read_data as rd


def main():


    #print(df_values)

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

    # Dictionary for eigenvalues of correlation matrix whose keys are regions.
    eigs = {i : [] for i in range(1,9)}

    for region in range(1,9):
        data = rd.get_data_for_region(region)
        predictors_region = data[predictors]
        M = predictors_region.corr()
        listeigs = (np.linalg.eigvals(M)).tolist()
        eigs[region] += listeigs




main()


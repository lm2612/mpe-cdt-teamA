import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import read_data as rd

LOB = 'LOB'
predictor_names = ['SUM_FREQ', 'AVERAGE_PGA_475yr',
                  'AVERAGE_SOIL', 'TOTAL_GDP',
                  'MEAN_MIPC', 'SUM_NIGHTLIGHTS',
                  'TOTAL_POP', 'SUM_SEISMIC_BUDGET',
                  'USGS_HISTORICAL_FREQ']

columns = ['region']
for predictor in predictor_names:
    columns.append(predictor)

correlations = pd.DataFrame(columns=columns)

for region in np.arange(1, 8):
    data = rd.get_data_for_region(region)
    row = [region]
    for predictor in predictor_names:
        model = ols(str(LOB)+' ~ '+str(predictor), data).fit()
        
        # make linear relationship
        X = np.linspace(min(data[predictor]), max(data[predictor]), 100)
        fitted_model = model._results.params[0] + X*model._results.params[1]

        row.append(model._results.params[1])
    correlations.loc[region] = row

print(correlations)

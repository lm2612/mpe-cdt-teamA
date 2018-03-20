# This code plots scatter plots for the individual predictors against
# LOB1 losses for region one. It then calculates polynomial fits, the degree
# of which is down to the user.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats import kurtosistest
from statsmodels.formula.api import ols
import read_data as rd

print(pd.__version__)

# Load csv ad a datafarme object using pandas
# IMPORTANT: THIS USES ALL THE DATA -- NEED TO ADD STRIPPING FOR TESTING
Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')
GDP = pd.read_csv('../AIR_data/Predictor_Data/GlobalGDP_Stats.csv')
GEMfr = pd.read_csv('../AIR_data/Predictor_Data/GEM_HistoricalFreq.csv')
GPGA = pd.read_csv('../AIR_data/Predictor_Data/Global475yrPGA.csv')
GSOIL= pd.read_csv('../AIR_data/Predictor_Data/GlobalAverageSoil.csv')
GMIPC = pd.read_csv('../AIR_data/Predictor_Data/GlobalMIPC_Stats.csv')
GNL = pd.read_csv('../AIR_data/Predictor_Data/Global_NightLights.csv')
GPop = pd.read_csv('../AIR_data/Predictor_Data/GlobalPopCounts.csv')
GSEIb = pd.read_csv('../AIR_data/Predictor_Data/GlobalSeismicBudget.csv')
USGSfr = pd.read_csv('../AIR_data/Predictor_Data/USGS_HistoricalFreq.csv')

Region_1_DR = pd.DataFrame(Region_1_DR)
Region_1_DR = Region_1_DR.sort(['AIRSID'])

# Select unique location ID in the AIRSID column
unique_arsid=Region_1_DR.AIRSID.unique()

aal = np.zeros((len(unique_arsid), 2))
GDP = GDP.loc[GDP['AIRSID'].isin(unique_arsid)]
GEMfr = GEMfr.loc[GEMfr['AIRSID'].isin(unique_arsid)]
GPGA = GPGA.loc[GPGA['AIRSID'].isin(unique_arsid)]
GSOIL = GSOIL.loc[GSOIL['AIRSID'].isin(unique_arsid)]
GMIPC = GMIPC.loc[GMIPC['AIRSID'].isin(unique_arsid)]
GNL = GNL.loc[GNL['AIRSID'].isin(unique_arsid)]
GPop = GPop.loc[GPop['AIRSID'].isin(unique_arsid)]
GSEIb = GSEIb.loc[GSEIb['AIRSID'].isin(unique_arsid)]

for i in range(0, len(unique_arsid)) :
	# For each unique AIRSID find the sum of LOB1
	aal[i, 0] = unique_arsid[i]
	aal[i, 1] = Region_1_DR.loc[Region_1_DR['AIRSID'] == unique_arsid[i], 'LOB1' ].sum()




#Some data missing AIRSIDs 10655, 10656 so ditch for ease (this is quick and dirty sorry!)
aal = np.delete(aal, (1,2), axis=0)
GDP = GDP.drop(GDP.index[[1,2]])
GSOIL = GSOIL.drop(GSOIL.index[[1,2]])
GMIPC = GMIPC.drop(GMIPC.index[[1,2]])
GNL = GNL.drop(GNL.index[[1,2]])
GPop = GPop.drop(GPop.index[[1,2]])


# Put into np.arrays
AALGDP = np.zeros((len(aal[:,0]), 3))
for i in range(0, len(aal[:,0])):
	AALGDP[i, 0] = aal[i, 0]
	AALGDP[i, 1] = aal[i, 1]
AALGDP[:,2] = GDP['TOTAL_GDP']

AALSUMF = np.zeros((len(aal[:,0]), 3))
for i in range(0, len(aal[:,0])):
	AALSUMF[i, 0] = aal[i, 0]
	AALSUMF[i, 1] = aal[i, 1]
AALSUMF[:,2] = GEMfr['SUM_FREQ']

print(len(AALGDP))

#AALSEIB = np.zeros((len(aal[:,0]), 3))
#for i in range(0, len(aal[:,0])):
#	AALSEIB[i, 0] = aal[i, 0]
#	AALSEIB[i, 1] = aal[i, 1]
#AALSEIB[:,2] = GSEIb['SUM_SEISMIC_BUGDET']

AALGDP = AALGDP[AALGDP[:,2].argsort()]
# remove bottom 5
AALGDP = AALGDP[:-5, :]
AALGDP = AALGDP[AALGDP[:,1].argsort()]
print(len(AALGDP))

plt.plot(AALGDP[:,2], AALGDP[:,1], '.')
plt.show()

#data = pd.DataFrame({'x': freq['AVERAGE_PGA_475yr'], 'y': aal[:,1]})

## Scatter plots of data

#f, axarr = plt.subplots(4, 2)
#plt.suptitle('Scatter plots of Predictors against losses in LOB1, Region 1')
#axarr[0,0].plot(GDP['TOTAL_GDP'], (aal[:,1]), 'bo')
#axarr[0, 0].set_title('GDP')
#axarr[0,1].plot(GEMfr['SUM_FREQ'], (aal[:,1]), 'bo')
#axarr[0, 1].set_title('SUM_FREQ')
#axarr[1,0].plot(GPGA['AVERAGE_PGA_475yr'], (aal[:,1]), 'bo')
#axarr[1, 0].set_title('AVERAGE_PGA_475yr')
#axarr[1,1].plot(GSOIL['AVERAGE_SOIL'], (aal[:,1]), 'bo')
#axarr[1, 1].set_title('AVERAGE_SOIL')
#axarr[2,0].plot(GMIPC['MEAN_MIPC'], (aal[:,1]), 'bo')
#axarr[2, 0].set_title('MEAN_MIPC')
#axarr[2,1].plot(GNL['SUM_NIGHTLIGHTS'], (aal[:,1]), 'bo')
#axarr[2,1].set_title('SUM_NIGHTLIGHTS')
#axarr[3,0].plot(GPop['TOTAL_POP'], (aal[:,1]), 'bo')
#axarr[3, 0].set_title('TOTAL_POP')
#axarr[3,1].plot(GSEIb['SUM_SEISMIC_BUDGET'], np.log(aal[:,1]), 'bo')
#axarr[3, 1].set_title('SUM_SEISMIC_BUGDET')
#plt.show()

## Fit polynomials
#GDPfit = np.polyfit(GDP['TOTAL_GDP'], (aal[:,1]), 1)
#GDPp = np.poly1d(GDPfit)
#GEMfrfit = np.polyfit(GEMfr['SUM_FREQ'], (aal[:,1]), 1)
#GEMfrp = np.poly1d(GEMfrfit)
#GPGAfit = np.polyfit(GPGA['AVERAGE_PGA_475yr'], (aal[:,1]), 1)
#GPGAp = np.poly1d(GPGAfit)
#GSOILfit = np.polyfit(GSOIL['AVERAGE_SOIL'], (aal[:,1]), 1)
#GSOILp = np.poly1d(GSOILfit)
#GMIPCfit = np.polyfit(GMIPC['MEAN_MIPC'], (aal[:,1]), 1)
#GMIPCp = np.poly1d(GMIPCfit)
#GNLfit = np.polyfit(GNL['SUM_NIGHTLIGHTS'], (aal[:,1]), 1)
#GNLp = np.poly1d(GNLfit)
#GPopfit = np.polyfit(GPop['TOTAL_POP'], (aal[:,1]), 1)
#GPopp = np.poly1d(GPopfit)
#GSEIbfit = np.polyfit(GSEIb['SUM_SEISMIC_BUDGET'], (aal[:,1]), 1)
#GSEIbp = np.poly1d(GSEIbfit)


#GDPX = np.linspace(min(GDP['TOTAL_GDP']), max(GDP['TOTAL_GDP']), 100)
#GEMX = np.linspace(min(GEMfr['SUM_FREQ']), max(GEMfr['SUM_FREQ']), 100)
#GPGAX = np.linspace(min(GPGA['AVERAGE_PGA_475yr']), max(GPGA['AVERAGE_PGA_475yr']), 100)
#GSOILX = np.linspace(min(GSOIL['AVERAGE_SOIL']), max(GSOIL['AVERAGE_SOIL']), 100)
#GMIPCX = np.linspace(min(GMIPC['MEAN_MIPC']), max(GMIPC['MEAN_MIPC']), 100)
#GNLX = np.linspace(min(GNL['SUM_NIGHTLIGHTS']), max(GNL['SUM_NIGHTLIGHTS']), 100)
#GPopX = np.linspace(min(GPop['TOTAL_POP']), max(GPop['TOTAL_POP']), 100)
#GSEIbX = np.linspace(min(GSEIb['SUM_SEISMIC_BUDGET']), max(GSEIb['SUM_SEISMIC_BUDGET']), 100)
	
	
#f, axarr = plt.subplots(4, 2)
#plt.suptitle('1d Linear Regressions for losses in Region 1, LOB1')
#axarr[0,0].plot(GDPX, GDPp(GDPX), 'r', GDP['TOTAL_GDP'], (aal[:,1]), 'bo')
#axarr[0, 0].set_title('GDP')
#axarr[0, 0].set_ylabel('LOB1 average annual loss')
#axarr[0,1].plot(GEMX, GEMfrp(GEMX), 'r', GEMfr['SUM_FREQ'], (aal[:,1]), 'bo')
#axarr[0, 1].set_title('SUM_FREQ')
#axarr[0, 1].set_ylabel('LOB1 average annual loss')
#axarr[1,0].plot(GPGAX, GPGAp(GPGAX), 'r', GPGA['AVERAGE_PGA_475yr'], (aal[:,1]), 'bo')
#axarr[1, 0].set_title('AVERAGE_PGA_475yr')
#axarr[1, 0].set_ylabel('LOB1 average annual loss')
#axarr[1,1].plot(GSOILX, GSOILp(GSOILX), 'r', GSOIL['AVERAGE_SOIL'], (aal[:,1]), 'bo')
#axarr[1, 1].set_title('AVERAGE_SOIL')
#axarr[1, 1].set_ylabel('LOB1 average annual loss')
#axarr[2,0].plot(GMIPCX, GMIPCp(GMIPCX), 'r', GMIPC['MEAN_MIPC'], (aal[:,1]), 'bo')
#axarr[2, 0].set_title('MEAN_MIPC')
#axarr[2, 0].set_ylabel('LOB1 average annual loss')
#axarr[2,1].plot(GNLX, GNLp(GNLX), 'r', GNL['SUM_NIGHTLIGHTS'], (aal[:,1]), 'bo')
#axarr[2,1].set_title('SUM_NIGHTLIGHTS')
#axarr[2, 1].set_ylabel('LOB1 average annual loss')
#axarr[3,0].plot(GPopX, GPopp(GPopX), 'r', GPop['TOTAL_POP'], (aal[:,1]), 'bo')
#axarr[3, 0].set_title('TOTAL_POP')
#axarr[3, 0].set_ylabel('LOB1 average annual loss')
#axarr[3,1].plot(GSEIbX, GSEIbp(GSEIbX), 'r', GSEIb['SUM_SEISMIC_BUDGET'], (aal[:,1]), 'bo')
#axarr[3, 1].set_title('SUM_SEISMIC_BUGDET')
#axarr[3, 1].set_ylabel('LOB1 average annual loss')
#plt.show()
	


import math
import pandas as pd
import numpy as np
from read_data import *
import matplotlib.pyplot as plt


def scatterplot(regiondata,inputdata,LOB='LOB1'):
	""" Scatter plot of loss for one region against one predictor input
	Arguments: regiondata is a pandas dataframe from output of getLOBdata for one region
	  	   inputdata is a pandas dataframe from output of predictor for one predictor 
		   LOB is string LOB1, LOB2, LOB3.... of what  you want to plot 
		  returns figure """
	inputname = list(inputdata)[1]

	# Add column to region data
	regiondata[inputname] = pd.Series() 

	for AIR_ID in inputdata['AIRSID']:
		if AIR_ID in list(regiondata['AIRSID']):
			# Add inputdata[inputname] to regiondata[inputname]
			regiondata[inputname] = inputdata[inputname]
		
	plt.plot(regiondata[inputname],regiondata[LOB],'ko')
	plt.xlabel(inputname)
	plt.ylabel(LOB)
			
inputfiles=['GEM_HistoricalFreq','Global_NightLights','Global475yrPGA','GlobalAverageSoil','GlobalGDP_Stats','GlobalMIPC_Stats','GlobalPopCounts','GlobalSeismicBudget','USGS_HistoricalFreq']
for inputfile in inputfiles:
	regiondata = getLOBdata('../AIR_data/Correct_loss_data/Region_1_DR.csv')
	regiondata = regiondata.sort_values('AIRSID')

	inputdata = predictor(inputfile+'.csv')

	fig = plt.figure()
	ax1 = plt.subplot2grid((3,1),(0,0))
	ax2 = plt.subplot2grid((3,1),(1,0))
	ax3 = plt.subplot2grid((3,1),(2,0))
	axes = [ax1,ax2,ax3]
	LOBS = ['LOB1','LOB2','LOB3']
	for ax,LOB in zip(axes,LOBS):
		plt.sca(ax)
		scatterplot(regiondata,inputdata,LOB)
	
	plt.savefig('../plots/Region1_%s.png'%inputfile)
	


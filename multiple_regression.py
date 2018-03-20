# A multiple-dimensional regression of all Predictors
# and a region of AALs (in this case Region One).
# WARNING: the fit is shit.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import read_data as rd

data = rd.get_data_for_region(4)
# Just do LOB1 for now
LOB = 'LOB'
# predictor are names of variables used in the multiple regression
headernames = list(data)
predictor = headernames[3:]
print(predictor)


x = data[predictor]
y = data[LOB]

x = sm.add_constant(x)

est = sm.OLS(y, x).fit()

#import pdb; pdb.set_trace()
params = est.params

#fit = params[0] + params[1] * data[predictor[0]] + params[2] * data[predictor[1]]
fit = params[0]
for i in range(len(predictor)):
	 fit = fit + params[i+1] * data[predictor[i]] 

conf = est.conf_int()
norm_conf0 = []
norm_conf1 = []
for i in range(len(predictor)+1):
	norm_conf0.append(conf[0][i]/list(est.params)[i])
	norm_conf1.append(conf[1][i]/list(est.params)[i])

conf['norm0']=norm_conf0
conf['norm1']=norm_conf1

print(conf)

#ax.scatter

plt.plot(fit, y, 'bo')
plt.show()


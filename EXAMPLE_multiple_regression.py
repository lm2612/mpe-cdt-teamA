"""
USEFUL CODE -- maybe?
Multiple Regression
====================

Calculate using 'statsmodels' just the best fit, or all the corresponding
statistical parameters.

n-dimensional linear regression
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas

# For 3d plots. This import is necessary to have 3D plotting below
from mpl_toolkits.mplot3d import Axes3D

# For statistics. Requires statsmodels 5.0 or more
from statsmodels.formula.api import ols
# Analysis of Variance (ANOVA) on linear models
from statsmodels.stats.anova import anova_lm

########################################################################
# Generate and show the data
x = np.linspace(-5, 5, 10)
# We generate a 3D grid
X, Y, Z = np.meshgrid(x, x, x)

# To get reproducable values, provide a seed value
np.random.seed(1)

# Create data
# Increasing coeff of noise will, obviously, reduce the goodness of fit
data = -5 + 3*X - 0.5*Y + 0.01*Z + 4 * np.random.normal(size=X.shape)


########################################################################
# Multilinear regression model, calculating fit, P-values, confidence
# intervals etc.

# Convert the data into a Pandas DataFrame to use the formulas framework
# in statsmodels

# First we need to flatten the data.
X1 = X.flatten()
Y1 = Y.flatten()
Z1 = Z.flatten()
D1 = data.flatten()

data = pandas.DataFrame({'x': X1, 'y': Y1, 'z': Z1, 'd' : D1})

# Fit the model
model = ols("d ~ x + y + z", data).fit()

# Print the summary
print(model.summary())

print("\nRetrieving manually the parameter estimates:")
print(model._results.params)


# Peform analysis of variance on fitted linear model
anova_results = anova_lm(model)

print('\nANOVA results')
print(anova_results)

plt.show()

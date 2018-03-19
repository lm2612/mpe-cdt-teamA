"""
USEFUL CODE -- maybe?
Multiple Regression
====================

Calculate using 'statsmodels' just the best fit, or all the corresponding
statistical parameters.

Also shows how to make 3d plots, in the case of bivariate data.
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
# We generate a 2D grid
X, Y = np.meshgrid(x, x)

# To get reproducable values, provide a seed value
np.random.seed(1)

# Create data
# Increasing coeff of noise will, obviously, reduce the goodness of fit
Z = -5 + 3*X - 0.5*Y + 4 * np.random.normal(size=X.shape)

# Plot the data
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm,
                      rstride=1, cstride=1)
ax.view_init(20, -120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

########################################################################
# Multilinear regression model, calculating fit, P-values, confidence
# intervals etc.

# Convert the data into a Pandas DataFrame to use the formulas framework
# in statsmodels

# First we need to flatten the data.
X1 = X.flatten()
Y1 = Y.flatten()
Z1 = Z.flatten()

data = pandas.DataFrame({'x': X1, 'y': Y1, 'z': Z1})

# Fit the model
model = ols("z ~ x + y", data).fit()

# Print the summary
print(model.summary())

print("\nRetrieving manually the parameter estimates:")
print(model._results.params)

# Shove them into function for plotting later
fitted_model = model._results.params[0] + X*model._results.params[1] + Y*model._results.params[2]

# Peform analysis of variance on fitted linear model
anova_results = anova_lm(model)

#print('\nANOVA results')
#print(anova_results)

# Plot the regression surface, superimposed with original data scattered
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, fitted_model, cmap=plt.cm.coolwarm,
                       rstride=1, cstride=1)
surf = ax.scatter(X, Y, Z, c='gray', s=10)
ax.view_init(20, -120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Estimated Z')

plt.show()

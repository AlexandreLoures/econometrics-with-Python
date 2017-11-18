##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##
##  ---                    maximum likelihood estimation                      ---  ##
##  ---                         by Alexandre Loures                           ---  ##
##  ---               Vicosa, Minas Gerais, Brazil 2017/11/14                 ---  ##
##  ---                          update 2017/11/18                            ---  ##
##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##

from numpy import exp

from scipy.misc import factorial

import matplotlib.pyplot as plt

poisson_pmf = lambda y, mu: mu**y / factorial (y) * exp (-mu)

y_values = range (0, 25)

fig, ax = plt.subplots (figsize = (12, 8))

for mu in [1, 5, 10]
    distribution = []
    for y_i in y_values:
        distribution.append (poisson_pmf (y_i, mu))
    ax.plot (y_values,
             distribution,
             label = ('$\mu$ = ' + str (mu)),
             alpha = .5,
             marker = 'o',
             markersize = 8)

ax.grid ()

ax.set_xlabel ('$y$', fontsize = 14)

ax.set_ylabel ('$f (y \mid \mu)$', fontsize = 14)

ax.axis (xmin = 0, ymin = 0)

ax.legend (fontsize = 14)

plt.savefig ('poisson_distribution.png')

plt.show ()

import pandas as pd
pd.options.dsiplay.max_columns = 10

##  reading stata extension file in Python

df = pd.read_stata ('C:\\Users\\Inspiron\\Desktop\\fp.dta')

##  examining the size of the database

df.shape

##  examining the first lines of the database

df.head ()

## using a histogram for visual analysis of the distribution of billionaries per country

numbil0_2008 = df [(df ['year'] == 2008) & (
    df ['country'] != 'United States')].loc [:, 'numbil0']

plt.subplots (figsize = (12, 8))

plt.hist (numbil0_2008, bins = 30)

plt.xlim (xmin = 0)

plt.grid ()

plt.xlabel ('Number of billionaries in 2008')

plt.ylabe ('Count')

plt.savefig ('histogram.png')

plt.show ()

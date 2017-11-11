##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##
##  ---                     linear regression in python                       ---  ##
##  ---                         by Alexandre Loures                           ---  ##
##  ---               Vicosa, Minas Gerais, Brazil 2017/11/10                 ---  ##
##  ---                          update 2017/11/10                            ---  ##
##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##

## database available in: https://raw.githubusercontent.com/RuiChang123/Regression_for_house_price_estimation/master/final_data.csv
## the version of python used was python 3.6.3

## changing directory in python

import os

os.chdir ('C:\\Users\\Inspiron\\Desktop')

## loading data to python

import pandas as pd

sf = pd.read_csv ('final_data.csv', sep = ';')

## visually analyzing the data

sf.head ()

sf.shape

sf.info ()

## discarding variables that are not of interest

sf.drop (sf.columns [[0, 2, 3, 15, 17, 18]], axis = 1, inplace = True)

sf.info ()

sf.describe ()

## converting datatype (dtype) object to float64 in pandas dataframe

sf ['zindexvalue'] = sf ['zindexvalue'].str.replace (',', '')

sf ['zindexvalue'] = pd.to_numeric (sf ['zindexvalue'])

sf.info ()

sf.describe ()

## analyzing visual data with graphs

import matplotlib.pyplot as plt

sf.hist (bins = 50, figsize (20, 15))

plt.savefig ('attribute_histogram_plots')

plt.show ()

## plotting a scatter with latitude and longitude

sf.plot (kind = 'scatter', x = 'latitude', y = 'longitude', alpha = .2)

plt.savefig ('map1.png')

## plotting a scatter with latitude and longitude showing color code from the most expensive to the least expesive areas

sf.plot (kind = 'scatter', x = 'latitude', y = 'longitude', alpha = .4, figsize = (10, 7), c = 'lastsoldprice', cmap = plt.get_cmap ('jet'), colorbar = True, sharex = False)

plt.savefig ('map2.png')

## looking how each independent variable correlates with this dependent variable

corr_matrix = sf.corr ()

corr_matrix ['lastsoldprice'].sort_values (ascending = False)

## looking the correlation between variables by using pandas' scatter_matrix function

from pandas.tools.plotting import scatter_matrix

attributes = ['lastsoldprice', 'finishedsqft', 'bathrooms', 'zindexvalue']

scatter_matrix (sf [attributes], figsize = (12, 8))

plt.savefig ('matrix.png')

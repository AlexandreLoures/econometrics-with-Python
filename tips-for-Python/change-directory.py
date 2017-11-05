##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##
##  ---        changing the directory and manipulating bases in python        ---  ##
##  ---                         by Alexandre Loures                           ---  ##
##  ---               Vicosa, Minas Gerais, Brazil 2017/11/05                 ---  ##
##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##


## changing directory

import os

os.chdir ("C:\\Users\\Inspiron\\OneDrive\\python\\base")


## reading csv extension file in python

import pandas

data = pandas.read_csv ('brain_size.csv', sep = ';', na_values = '.')


## estimating a generalized linear model

import pandas as pd

python = pd.read_csv ('python.csv', sep = ';', na_values = '.')

import statsmodels.api as sm

import statsmodels.fomula.api as smf

reg = smf.glm ('trade ~ rta + ldist + cntg + lang + clny', python, family = sm.families.Poison ()).fit ()

reg.summary ()

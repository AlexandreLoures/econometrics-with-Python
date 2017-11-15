##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##
##  ---                    maximum likelihood estimation                      ---  ##
##  ---                         by Alexandre Loures                           ---  ##
##  ---               Vicosa, Minas Gerais, Brazil 2017/11/14                 ---  ##
##  ---                          update 2017/11/14                            ---  ##
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

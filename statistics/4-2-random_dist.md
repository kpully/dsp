[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import random
t = [random.random() for _ in range(1000)]
import pandas as pd
import numpy as np
import math
import thinkplot

pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

cdf = thinkstats2.Cdf(t, label='totalwgt_lb')
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='percentile rank', ylabel='CDF')
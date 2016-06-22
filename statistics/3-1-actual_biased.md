[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> REPLACE THIS TEXT WITH YOUR RESPONSE
import pandas as pd
import numpy as np
import math
import thinkplot


import thinkstats2
import chap01soln
resp = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh)
pmf


def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf



biased = BiasPmf(pmf, label='biased')



thinkplot.preplot(2)
thinkplot.Pmfs([pmf, biased])
f = thinkplot.Show(xlabel='class size', ylabel='PMF')

print('pmf mean', pmf.Mean())
print('biased pmf mean', biased.Mean())
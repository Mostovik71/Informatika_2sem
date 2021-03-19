import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import stats
df = pd.read_csv('r4z2.csv')
pd.crosstab(df['X'], df['Y'])
dfx=df['X'].tolist()
dfy=df['Y'].tolist()
fa=zip(dfx,dfy)
chi2, prob, df, expected = stats.chi2_contingency(fa)

output = "test Statistics: {}\ndegrees of freedom: {}\np-value: {}\n"

print(output.format( chi2, df, prob))

print(expected)
#print(table)
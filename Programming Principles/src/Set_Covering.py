import numpy as np
from gurobipy import *

N = 10
probTresh = 0.5

mA = np.random.uniform(0., 1., (N, N))
mA = np.triu(mA, k=0)
mA[mA > probTresh] = 1
mA[mA <= probTresh] = 0
mA[:,0] = 1
mA[0,:] = 1
print(mA)
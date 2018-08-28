'''
vars.py

Purpose:
    ...

Version:
    0            Assign/print String
    
Date:
    28 Aug 2018
    
@author: jbn601
'''
########################################################
### Imports
import numpy as np
# import scipy as sp
# import matplotlib.pyplot as plt
# from gurobi import *

#######################################################
### Main
def main():
    # Magic numbers
    sA = "String"
    iB = 1
    dC = 1.
    bD = ((9 > 11) and (3 < 1)) or (type(iB) == type(dC))
    lE = [1, 2, 3, "Test", True]
    lF = [[1, 2, 3], ["Nice", "Beautiful"]]
    mG = np.array([[1, 2], [3, 4]])
    fnH = np.array
    # Initialisation
    
    # Output
    print("The String I choose is \"%s\".\n" % (sA))
    print("The Integer I choose is \"%i\".\n" % (iB))
    print("The Double I choose is \"%.2g\".\n" % (dC))
    print("The Boolean I choose is very complicated and equal to \"%r\".\n" % (bD))
    print("I have made the following beautiful list \"%r\".\n" % (lE))
    print("I have also made a 2-D list \"%r\".\n" % (lF))
    print("I also have a beautiful matrix: \"%r\".\n" % (mG))
    print(fnH)
####################################################
### start main
if __name__ == '__main__':
    main()
    
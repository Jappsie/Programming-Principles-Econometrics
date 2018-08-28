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
# import numpy as np
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
    # Initialisation
    
    # Output
    print("The String I choose is \"%s\".\n" % (sA))
    print("The Integer I choose is \"%i\".\n" % (iB))
    print("The Double I choose is \"%.2g\".\n" % (dC))
    print("The Boolean I choose is very complicated and equal to \"%r\".\n" % (bD))
    
####################################################
### start main
if __name__ == '__main__':
    main()
    
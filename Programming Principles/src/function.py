'''
C:/Users/jaspe/Documents/School/VU/Python Programming/VU/TestProject/src/function.py
Purpose:
    ...

Version:
    1            First Starts
    
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
### printStr
def printStr(sIn):
    '''
    Purpose:    
        Prints the given argument.
    Inputs:
        sIn        String, argument to print
    Return value:
    '''
    # Magic numbers
    
    # Initialisation
    
    # Output
    print(sIn)
    
#######################################################
### passValue
def passValue():
    '''
    Purpose:
        Assign a predetermined (random) value
    Inputs:
        
    Return value:
        dRes        double, assigned random value
    '''
    # Magic numbers
    dRes = np.random.normal(0, 10, 1)
    # Initialisation
    
    # Output
    return dRes
#######################################################
### Main
def main():
    # Magic numbers
    sA = "Getal"
    # Initialisation
    dB = passValue()
    # Output
    printStr(sA)
    print(dB)
    
####################################################
### start main
if __name__ == '__main__':
    main()
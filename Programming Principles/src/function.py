'''
C:/Users/jaspe/Documents/School/VU/Python Programming/VU/TestProject/src/function.py
Purpose:
    Fun with functions

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
### passValues
def passValues():
    '''
    Purpose:
        Assign two predetermined (random) values
    Inputs:
        
    Return value:
        dRes1        double, assigned random value
        dRes2        double, assigned random value
    '''
    # Magic numbers
    dRes1 = np.random.normal(0,1,1)
    dRes2 = np.random.exponential(10,1)
    # Initialisation
    
    # Output
    return dRes1, dRes2
#######################################################
### Main
def main():
    # Magic numbers
    sA = "Getal"
    # Initialisation
    np.random.seed(9999)
    dB = passValue()
    dC,dD = passValues()
    # Output
    printStr(sA)
    print(dB)
    print(dC)
    print(dD)
    
####################################################
### start main
if __name__ == '__main__':
    main()
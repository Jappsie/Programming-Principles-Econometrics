'''
C:/Users/jaspe/Documents/School/VU/Programming Bootcamp/Programming Principles/src/backsubstitution.py
Purpose:
    Performs backsubstitution on the given system of linear equations

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
### findMax
def findMax(mA):
    '''
    Purpose:
        Finds the largest element of a matrix
    Input:
        mA             np.array, a matrix
    Return value:    
        dRes           double, the largest element of the matrix
    '''
    # Magic numbers
    
    # Initialisation
    dRes = mA[0,0]
    
    # Output
    n = np.size(mA,0)
    k = np.size(mA,1)
    for i in range(n):
        for j in range(k):
            if mA[i,j] > dRes:
                dRes = mA[i,j]
        
    return dRes
#######################################################
### findMin
def findMin(mA):
    '''
    Purpose:
        Finds the smallest element of a matrix
    Input:
        mA             np.array, a matrix
    Return value:    
        dRes           double, the smallest element of the matrix
    '''
    # Magic numbers
    
    # Initialisation
    dRes = findMax(-mA)
    # Output
    return -1*dRes

#######################################################
### Main
def main():
    # Magic numbers
    mA = np.array([[6.0, -2.0, 2.0, 4.0],
                   [0., -4., 2., 2.],
                   [0., 0., 2., -5.],
                   [0., 0., 0., -3.]])
    vb = np.array([[16.0],[-6.],[-9.],[-3.]])
    # Initialisation
    
    # Output
    print("The matrix we are working with is equal to \n", mA)
    print("The vector we are working with is equal to \n", vb)
    print("The largest element of our matrix is ", findMax(mA))
    print("The smallest element of our vector is ", findMin(vb))
    
####################################################
### start main
if __name__ == '__main__':
    main()
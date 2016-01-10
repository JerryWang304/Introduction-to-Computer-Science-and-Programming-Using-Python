# -*- coding: utf-8 -*-
def isPrime(x):
    if x<=1:
       return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
        
def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    ret = []
    for i in range(2,N+1):
        if isPrime(i):
            ret = ret + [i,]
    return ret
        

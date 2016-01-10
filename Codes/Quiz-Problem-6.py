def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N/10 == 0:
        if N%10 == 7:
            return 1
        else:
            return 0
    else:
        return count7(N%10) + count7(N/10)
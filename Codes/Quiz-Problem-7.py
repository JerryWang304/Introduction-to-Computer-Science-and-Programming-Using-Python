def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    ret = []
    for key in aDict.keys():
        second = None
        for k in aDict.keys():
            if k != key and aDict[k] == aDict[key]:
               second = k 
        if second == None:
            ret = ret + [key,]
    return ret
#print uniqueValues({1:2,3:2,4:9,0:8,7:4})
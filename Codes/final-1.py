def getSublists(L,n):
    ret = []
    for i in range(len(L)):
        temp = []
        if i + n <= len(L):
            for j in range(n):
                temp.append(L[i+j])
            ret.append(temp)
    return ret
#print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 9, 2],4)        
def longestRun(L):
    ans = 1
    for i in range(len(L)):
        j = i+1
        count = 1
        while j < len(L) and L[j]>=L[j-1]:
            count += 1
            j += 1
        if count>ans:
            ans = count
    return ans
#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 0, 2])           
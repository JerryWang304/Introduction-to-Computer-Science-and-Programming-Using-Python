s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if i+2 < len(s) and s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count+=1
print 'Number of times bob occurs is: ' + str(count)
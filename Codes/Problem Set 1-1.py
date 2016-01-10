
s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i] in ['a','e','i','o','u']:
        count +=1
print 'Number of vowels: ' + str(count)
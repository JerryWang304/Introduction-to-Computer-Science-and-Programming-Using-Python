s = 'azcbobobegghakl'
index = 0
length = 1
for x in range(len(s)):
    j = x+1
    count = 1
    while j < len(s) and s[j] >= s[j-1]:
        count+=1
        j+=1
    if count > length:
        length = count
        index = x
ans = ''

while length>0:
    ans += s[index]
    index +=1
    length -= 1
print 'Longest substring in alphabetical order is: '+ans
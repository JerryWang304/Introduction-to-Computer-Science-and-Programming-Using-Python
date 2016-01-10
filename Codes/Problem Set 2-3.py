#Test Case 1
balance = 320000
annualInterestRate = 0.2
low = balance/12.0
high = balance*((1+(annualInterestRate/12))**12)/12.0
ans = 0
def remain(balance,ans,annualInterestRate):
    for i in range(12):
        balance -= ans
        balance += balance*annualInterestRate/12.0
        
    return balance

left = balance
while abs(left-0)>0.01:
    if left>0:
        low = ans
    else:
        high = ans
    ans = (low+high)/2
    left = remain(balance,ans,annualInterestRate)
print 'Lowest Payment: '+str(round(ans,2))
    
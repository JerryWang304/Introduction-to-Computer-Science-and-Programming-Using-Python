#Test Case 2
balance = 4773
annualInterestRate = 0.2
ans = 1
def left(balance, ans, annualInterestRate):
    for i in range(12):
        balance = balance - ans*10
        balance = balance*(1+annualInterestRate/12.0)
    return balance
while left(balance,ans,annualInterestRate) > 0:
    ans+=1
print 'Lower Payment: ' + str(ans*10)
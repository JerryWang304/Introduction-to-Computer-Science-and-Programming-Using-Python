#Test Case 1
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPayment = 0.0
for i in range(12):
    print 'Month: ' + str(i+1)
    minimalMonthPayment = balance * monthlyPaymentRate
    balance -= minimalMonthPayment
    balance = balance + balance*annualInterestRate/12.0
    print 'Minimum monthly payment: ' + str(round(minimalMonthPayment,2))
    print 'Remaining balance: ' + str(round(balance,2))
    totalPayment+=minimalMonthPayment
print 'Total paied: ' + str(round(totalPayment,2))
print 'Remaining balance: ' + str(round(balance,2))
    
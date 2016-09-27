# Write a program to calculate the credit card balance after one year if a person only
# pays the minimum monthly payment required by the credit card company each
# month.
balance = float(input("Please, еnter your start balance "))
annualInterestRate = float(input("Please, еnter your annualInterestRate "))
paymentrate = float(input("Please, еnter your monthlyPaymentRate "))

monthlyInterestRate = annualInterestRate / 12.0
n = 0
totalpaid = 0
for n in range(1, 13):
    payment = balance * paymentrate
    balancestay = balance - payment
    newbalance = balancestay + (monthlyInterestRate * balancestay)
    n+=1
    balance = newbalance
    totalpaid += payment
    print("Month: ", n-1)
    print("Minimum monthly payment: ", "%.2f" % payment)
    print("Remaining balance: ", "%.2f" % newbalance)
print("Total paid: ", "%.2f" % totalpaid)

#Now write a program that calculates the minimum fixed monthly payment needed
#in order pay off a credit card balance within 12 months. By a fixed monthly
#payment, we mean a single number which does not change each month, but
#instead is a constant amount that will be paid each month.

balance = float(input("Please, еnter your start balance "))
annualInterestRate = float(input("Please, еnter your annualInterestRate "))
monthlyInterestRate = annualInterestRate / 12.0
payment = 10
n = 0
newbalance = balance
while newbalance >= payment:
         balancestay = balance - payment
         newbalance = balancestay + (monthlyInterestRate * balancestay)
         balance = newbalance
         payment += 10
print("Lowest Payment: ", payment)

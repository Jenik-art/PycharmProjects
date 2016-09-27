#Now write a program that calculates the minimum fixed monthly payment needed
#in order pay off a credit card balance within 12 months. By a fixed monthly
#payment, we mean a single number which does not change each month, but
#instead is a constant amount that will be paid each month.
print("Please, еnter your start balance")
balance = float(input())
print("Please, еnter your annualInterestRate")
procentInyear = float(input())

procentInmonth = procentInyear / 12.0
payment = 10
n = 0
newbalance = balance
while newbalance >= payment:

         balancestay = balance - payment
         newbalance = balancestay + (procentInmonth * balancestay)
         balance = newbalance

         payment += 10
print("Lowest Payment: ", payment)

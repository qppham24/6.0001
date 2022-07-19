from math import ceil
import random

#user input
annual_salary = float(input("Enter the starting salary: "))

#assumptions
down_payment = 0.25 * 1000000
steps = 0
monthly_salary = annual_salary / 12

def amountSaved(monthly_salary, rate):
    savings = 0
    for i in range(36):
        if i%6 == 0:
            monthly_salary += monthly_salary * 0.07
        savings += savings * (0.04 /12)
        savings += monthly_salary * rate
    return savings

min = 0
max = 10000
rate = (min + max) / 2

while min <= max: 
    steps += 1
    rate = ceil((min + max) / 2)
    savings = amountSaved(monthly_salary, rate/10000)
    if savings >= down_payment - 100 and savings <= down_payment + 100: 
        print("Best savings rate is: " + str(rate/10000))
        print("Steps in bisection search: " + str(steps))
        exit()
    if savings < down_payment:
        min = rate + 1
    if savings > down_payment:
        max = rate - 1
print("It is not possible to pay the down payment in three years.")
#user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12


def timeToSave(saved, monthly, portion, down):
    month = 0
    while saved < down:
        month += 1
        saved += saved * (0.04 /12)
        saved += monthly * portion
    return month
    
print("Number of months: " + str(timeToSave(current_savings, monthly_salary, portion_saved, portion_down_payment)))
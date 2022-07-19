#user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))


portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12


def timeToSave(saved, monthly, portion, down, salary_raise):
    month = 0
    while saved < down:
        month += 1
        if month%6 == 0:
            monthly += monthly * salary_raise
        saved += saved * (0.04 /12)
        saved += monthly * portion
    return month
    
print("Number of months: " + str(timeToSave(current_savings, monthly_salary, portion_saved, portion_down_payment, semi_annual_raise)))
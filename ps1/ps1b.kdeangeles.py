### Gather User Input ###
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

### Initialize Variables ###
portion_down_payment = total_cost * 0.25
current_savings = 0.00
current_months = 0
r = 0.04

while current_savings < portion_down_payment:

    amount_saved = annual_salary / 12 * portion_saved
    current_savings += amount_saved

    investment_return = current_savings * r / 12
    current_savings += investment_return

    if current_months % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

    current_months += 1

print("Number of months: " + str(current_months))
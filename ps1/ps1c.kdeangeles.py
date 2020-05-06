### Gather User Input ###
init_annual_salary = float(input("Enter the starting salary: "))

### Set variables ###
portion_saved = 0.00 # Percentage of salary saved.  We need to figure this out
total_cost = 1000000.00 # Cost of house is $1M
semi_annual_raise = 0.07 # Expect to get 7% raise every 6 months
down_payment = total_cost * 0.25 # Target is 25% down payment
r = 0.04 # Expect 4% return on investments annually
current_savings = 0.00 # What we have in the bank

### Set loop and bisection search variables ###
high = 10000 # 100% as int, avoid using float
low = 0
num_guesses = 0
guess = (high + low) / 2
epsilon = 100.00 # Get within $100 of the down payment
goal_reached = False

while not goal_reached:
    
    ### Perform bisection search to determine savings rate to test
    current_savings = 0.00 # Reset current savings
    annual_salary = init_annual_salary # Reset annual salary to user provided value
    guess = int((high + low) / 2) # Recalculate guess
    portion_saved = guess / 10000 # convert guess to float to use as a percentage

    ### Run the "simulation" for 36 months
    for month in range(1, 37):

        ### Divide annual salary and multiply by portion_saved and add to current savings
        amount_saved = annual_salary / 12 * portion_saved
        current_savings += amount_saved

        ### Calculate the investment return in the current savings and add it back into the current savings
        investment_return = current_savings * r / 12
        current_savings += investment_return

        ### Raise by semi_annual_raise every 6 months
        if month % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)

    ### Did our current_savings get within $100 of our down payment goal?
    if abs(down_payment - current_savings) >= epsilon:

        ### If percentage of savings is greater than 99.99%, it's not possible.  Exit.
        if guess >= 9999:
            print("It is not possible to pay the down payment in three years.")
            exit()

        num_guesses += 1 # Increment number of steps in bisection search

        ### Recalculate values for next iteration of bisection search
        if current_savings < down_payment:
            low = guess # We didn't save enough - need to try with a higher savings percentage

        else:
            high = guess # We saved too much - need to try with a lower savings percentage

    else:
        goal_reached = True

### Print results and exit
print("Best savings rate: " + str(guess / 10000))
print("Steps in bisection search: " + str(num_guesses))
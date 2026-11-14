# 1.3 --------------------------------
###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')
# 1.4 --------------------------------
###
# Credit card payment 
#
account_balance = 500
total_payment = int(input('Enter your price: '))
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
# sprawdzenie dzialania
#
account_balance = 500
total_payment = int(input('Enter your price: '))
Enter your price: 140
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
Payment completed
#
account_balance = 500
total_payment = int(input('Enter your price: '))
Enter your price: 499
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
Payment completed
#
account_balance = 500
total_payment = int(input('Enter your price: '))
Enter your price: 500
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
Payment completed
#
account_balance = 500
total_payment = int(input('Enter your price: '))
Enter your price: 501
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
No funds
#
account_balance = 500
total_payment = int(input('Enter your price: '))
Enter your price: 720
if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')
No funds
# 1.5 ---------------------------------
###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('Enter an amount of your correctly completed tasks: '))
test_passed = False

# 50% of total_tasks is 10
if tasks_ok >= total_tasks / 2:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
# sprawdzenie dzialania
Enter an amount of your correctly completed tasks: 20
Congratulations! You passed the test.
#
Enter an amount of your correctly completed tasks: 11
Congratulations! You passed the test.
#
Enter an amount of your correctly completed tasks: 10
Congratulations! You passed the test.
#
Enter an amount of your correctly completed tasks: 9
Unfortunately, you failed the test.
#
Enter an amount of your correctly completed tasks: 0
Unfortunately, you failed the test.
#
# 1.6 --------------------------------
###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
# 1.7 --------------------------------
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = (basic_salary * bonus) + basic_salary
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')
# sprawdzenie dzialania
#
Does the employee receive a bonus? (Y/N):N
Basic salary: 5000
Bonus included? False
Total salary: 5000
#
Does the employee receive a bonus? (Y/N):Y
Basic salary: 5000
Bonus included? True
Total salary: 6500.0

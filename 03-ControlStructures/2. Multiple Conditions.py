# 2.2 -----------------------------------------
###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol.')
# test dzialania
Enter size symbol: S
S: Small size
#
Enter size symbol: M
M: Medium size
#
Enter size symbol: L
L: Large size
#
Enter size symbol: XL
XL: Extra large size
#
Enter size symbol: XXL
Incorrect symbol.
# 2.3 ---------------------------------------------
###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9 
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    fuel_consumption = 0

total_consumption = (fuel_consumption * distance) / 100
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
# sprawdzenie dzialania
Enter driving mode (A/M/E): M
Enter distance in km: 200
Total fuel consumption over a distance of 200 km in driving mode M is 18.0 liters
#
Enter driving mode (A/M/E): A
Enter distance in km: 400
Total fuel consumption over a distance of 400 km in driving mode A is 28.0 liters
#
Enter driving mode (A/M/E): E
Enter distance in km: 350
Total fuel consumption over a distance of 350 km in driving mode E is 21.0 liters
# 2.4 -----------------------------------------------
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = 'Error: Division by zero'
else:
    result = 'Error: Invalid operator'

# print result
print(f'{number1} {operator} {number2} = {result}')
# sprawdzenie dzialania
Enter first number: 2
Enter second number: 3
Enter operator (+, -, *, /): +
2.0 + 3.0 = 5.0
#
Enter first number: 2
Enter second number: 4
Enter operator (+, -, *, /): *
2.0 * 4.0 = 8.0
#
Enter first number: 3
Enter second number: 5
Enter operator (+, -, *, /): -
3.0 - 5.0 = -2.0
#
Enter first number: 5
Enter second number: 6
Enter operator (+, -, *, /): *
5.0 * 6.0 = 30.0
# 2.5 ------------------------------------------------
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
else:
    quarter = 'Invalid month'

print(f'Month {month} is in quarter {quarter}')
# sprawdzanie dzialania programu
Enter month number (1..12): 12
Month 12 is in quarter 4
#
Enter month number (1..12): 10
Month 10 is in quarter 4
#
Enter month number (1..12): 9
Month 9 is in quarter 3
#
Enter month number (1..12): 1
Month 1 is in quarter 1
# 2.6 --------------------------------------------------
# Program that checks what number was entered from the keyboard
#
number = int(input('Enter a number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')
# sprawdzenie dzialania
Enter a number: 7
Number 7 is positive
#
Enter a number: 1
Number 1 is positive
#
Enter a number: 0
Number is 0
#
Enter a number: -1
Number -1 is negative
#
Enter a number: -4
Number -4 is negative
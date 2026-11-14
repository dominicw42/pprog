# 7.1 --------------------------------------
###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
no_tax = age <= 26 # boolean expression
print(f'Exemption from paying taxes: {no_tax}')
# sprawdzenie zadania na podstawie podanych liczb
age = int(input('Enter age: '))
Enter age: 38
no_tax = age <= 26 
print(f'Exemption from paying taxes: {no_tax}')
Exemption from paying taxes: False
#
age = int(input('Enter age: '))
Enter age: 27
no_tax = age <= 26 
print(f'Exemption from paying taxes: {no_tax}')
Exemption from paying taxes: False
#
age = int(input('Enter age: '))
Enter age: 26
no_tax = age <= 26
print(f'Exemption from paying taxes: {no_tax}')
Exemption from paying taxes: True
#
Enter age: 22
no_tax = age <= 26 
print(f'Exemption from paying taxes: {no_tax}')
Exemption from paying taxes: True
#
age = int(input('Enter age: '))
Enter age: 18
no_tax = age <= 26 
print(f'Exemption from paying taxes: {no_tax}')
Exemption from paying taxes: True
# 7.2 --------------------------------------
###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
# sprawdzenie zadania na podstawie podanych hasel 
password = input('Enter password: ')
Enter password: university
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
Password length is valid: True
#
password = input('Enter password: ')
Enter password: peter123
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
Password length is valid: True
#
password = input('Enter password: ')
Enter password: seven
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
Password length is valid: False
#
password = input('Enter password: ')
Enter password: anna333
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
Password length is valid: False
# 7.3 --------------------------------------
###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#
number = int(input('Enter number: '))
even = number % 2 == 0 # modulo sprawdza resztę z dzielenia; gdy jest 0, liczba jest parzysta
print(f'Number is even: {even}')
# sprawdzenie zadania na podstawie podanych liczb
number = int(input('Enter number: '))
Enter number: 24
even = number % 2 == 0
print(f'Number is even: {even}')
Number is even: True
#
number = int(input('Enter number: '))
Enter number: 8
even = number % 2 == 0
print(f'Number is even: {even}')
Number is even: True
#
number = int(input('Enter number: '))
Enter number: 31
even = number % 2 == 0
print(f'Number is even: {even}')
Number is even: False
#
number = int(input('Enter number: '))
Enter number: 5
even = number % 2 == 0
print(f'Number is even: {even}')
Number is even: False
# 7.4 --------------------------------------
circumference = float(input('Wpisz obwód: '))
diameter = circumference / 3.14
diameter_ok = diameter >= 50
print(f'Tree can be cut down: {diameter_ok}')
# sprawdzenie zadania na podstawie podanych liczb
circumference = float(input('Wpisz obwód: '))
Wpisz obwód: 160
diameter = circumference / 3.14
diameter_ok = diameter >= 50
print(f'Tree can be cut down: {diameter_ok}')
Tree can be cut down: True
#
circumference = float(input('Wpisz obwód: '))
Wpisz obwód: 90
diameter = circumference / 3.14
diameter_ok = diameter >= 50
print(f'Tree can be cut down: {diameter_ok}')
Tree can be cut down: False
#
circumference = float(input('Wpisz obwód: '))
Wpisz obwód: 230
diameter = circumference / 3.14
diameter_ok = diameter >= 50
print(f'Tree can be cut down: {diameter_ok}')
Tree can be cut down: True
#
circumference = float(input('Wpisz obwód: '))
Wpisz obwód: 120
diameter = circumference / 3.14
diameter_ok = diameter >= 50
print(f'Tree can be cut down: {diameter_ok}')
Tree can be cut down: False
# 7.5 --------------------------------------
###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number')
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
print(f'Car is from Krakow: {is_krakow}')
# 7.6 --------------------------------------
vehicle_speed = int(input('Enter vehicle speed: '))
speed_limit = vehicle_speed >= 40 and vehicle_speed <= 140
print(f'Speed is valid: {speed_limit}')
# 7.7 --------------------------------------
import random # importing the "random" module 
random_number = random.randint(5,10) # choosing a random number between 5 and 10
print(random_number) 
# test programu
import random
random_number = random.randint(5,10)
print(random_number)
10
#
import random
random_number = random.randint(5,10)
print(random_number)
7
#
import random
random_number = random.randint(5,10)
print(random_number)
8
#
import random
random_number = random.randint(5,10)
print(random_number)
6
#
import random
random_number = random.randint(5,10)
print(random_number)
6
# 7.8 --------------------------------------
###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(total)
# 7.9 --------------------------------------
import random
dice_roll = random.randint(1,6)
special = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number: {special}')
# 7.10 --------------------------------------
###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input('Write your guess (1-6):'))
win = computer == you
print(f'You won: {win}')
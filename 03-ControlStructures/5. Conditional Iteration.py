# 5.4 -------------------------------------
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
# 5.5 -------------------------------------
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number
    count += 1

if count > 0:
    arithmetic_mean = total_sum / count
else:
    arithmetic_mean = 0

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean is: {arithmetic_mean}")
# 5.6 -------------------------------------
N = 10
sum_even = 0
i = 1

# Calculate the sum of even numbers using a while loop
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
# 5.7 -------------------------------------
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown == 5:
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    else:
        print(countdown)
        
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
# 5.8 -------------------------------------
###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check your PIN")
    print("5. Change your PIN")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print(f'Your pin is {pin}')
    elif choice == '5':
        newpin = input('Enter new PIN: ')
        if newpin.isdigit() and len(newpin) == 4:
            print('Your pin has been changed.')
            pin = newpin
        else:
            print('PIN is in incorrect format.')
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")

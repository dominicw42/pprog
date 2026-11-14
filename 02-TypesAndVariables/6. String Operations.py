# 6.1 ------------------------------------
###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Anna'   # replace Anna with your name
surname = 'May' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_full_name = len(name + " " + surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters') # with a space between name and surname
# 6.2 ------------------------------------
###
# A program that prints your initials
#
name = 'George'
surname = 'Soros'
print(name[0])
print(surname[0])
# 6.3 ------------------------------------
###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
abbreviation = university[0] + university[7] + university[15]
print(abbreviation)
# 6.4 ------------------------------------
###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:32]}')
print(f'Initials: {employee[4:8]} {employee[9:12]}')
# 6.5 ------------------------------------
###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'Phone number: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}')
# 6.6 ------------------------------------
###
# A program to print numerical representations of characters.
#
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')
# 6.7 ------------------------------------
###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Dominic' # replace John with your name
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')
print(f'The letter {name[5]} has a code {ord(name[5])}')
print(f'The letter {name[6]} has a code {ord(name[6])}')
print(f'The letter {name[7]} has a code {ord(name[7])}')
# 6.8 ------------------------------------
###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(last_letter_code - first_letter_code) - 1 #<-- zmiana na wartość bezwględną, aby uniknąć ujemnych wyników; dodanie -1, aby zmierzyc wylacznie litery pomiędzy nimi
print(f'Between {first} and {last} is {number_of_letters} letters')
# 6.9 ------------------------------------
###
# Character code conversion
#
print(chr(67),chr(111),chr(111),chr(108),chr(33))
# 6.10 ------------------------------------
###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Number of characters: ', movie.upper())

# print title in small letters
print('Number of characters: ', movie.lower())

# print how many times the vowel "e" appears in the title
print('Number of times "e" appears: ', movie.count('e'))

# print where in the text is the word "Lord"
print('Position of "Lord": ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('Position of "dragon": ', movie.find('dragon'))

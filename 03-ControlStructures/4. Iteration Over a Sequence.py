# 4.3 ----------------------------------------
for i in range(4):
    print('Practice makes perfect!')
# 4.4 ----------------------------------------
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)             # original university name
print(university_expanded)    # expanded university name
# 4.5 ----------------------------------------
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    new_char = chr(ord(char) + 1)
    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)
# 4.6 ----------------------------------------
total_sum = 0

for i in range(5, 11):
    total_sum += i

print(f'Sum is {total_sum}')
# 4.7 ----------------------------------------
sum_even = 0

for i in range(1, 11):
    if i % 2 != 0: 
        continue
    sum_even += i

print(f'Sum of even numbers in the range <1,10> is {sum_even}')
# 4.8 ----------------------------------------
for i in range(1, 11):
    print(f'1/{i} = {1 / i}')
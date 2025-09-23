"""
Create a Python script that asks the user for a number and then
prints out a list of all the divisors of each number less than the asked number.
"""
x = int(input("Enter a number: "))
all_divisors = list()

for i in range(2, x//2+1):
    if x%2 == 0:
        all_divisors.append(i)

print(all_divisors)

"""
Write a Python program to check if an integer (x) is the power of another integer (y). 
Prompt the user to input both integers.
Input: 16, 2
Output: 2 ** 4 = 16
"""
x = int(input("Enter the First digit: "))
y = int(input("Enter the second digit: "))
found = False
for i in range(2, x//2):
    if y ** i == x:
        print(f"{y} ** {i} = {x}")
        found = True
        break
else:
    print(f"{x} is not a power of {y} ")

"""
Write a Python program that counts and displays the vowels 
of a given string ignoring the letter case.
"""
#User Input
text = input("Enter a text: ")

#Initialize the vowels
vowels = 'aeiou'

#Initializing a counter
count = 0

lower_text = text.lower()
for char in lower_text:
    if char in vowels:
        print(char, end="")
        count += 1

print(f"The Total Number of Vowels Found{count}")


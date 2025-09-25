# Create a Python script that removes all the occurrences of a given element of a list.
rl = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
n = 1
while n in rl:
    rl.remove(n)
print(rl)

# Create a Python script that removes all the elements of a list that are duplicate.
l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
unique_list = []
for n in l1:
    if n not in unique_list:
        unique_list.append(n)
print(unique_list)

"""
Consider the following string: nums = '10,20,30,40,50'
Create a Python script that creates a list of integers from the string.
The resulting list will be: [10, 20, 30, 40, 50]
"""
nums = '10,20,30,40,50'
nums_list = nums.split(',')
print(nums_list)
nums1 = [int(n) for n in nums_list ]
print(nums1)

"""Write a Python script which finds all numbers that are divisible by 7 but are not a
 multiple of 5, between 1500 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence (csv) on a single line.
"""
nums = list()

for n in range(1500, 32001):
    if n % 7 == 0 and n % 5 != 0:
        nums.append(str(n))
print(','.join(nums))

"""Write a program that asks the user for a long string containing 
multiple words separated by whitespaces.
Print back to the user the same string with the words in backwards order.
"""
words = input("Enter some words: ")
words_list = words.split(' ')
words_reversed = ' '.join(reversed(words_list))
print(words_reversed)
"""
Write a Python program that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
"""
string = input("Enter a hyphen separated string: ")
string_list = string.split('-')
string_sorted = sorted(string_list)
sorted_string = '-'.join(string_sorted)
print(sorted_string)

"""
Write a Python program that accepts as input a sequence of words separated by one
or more whitespaces and prints out the same words with the letters in reversed order.
Do not use list comprehension.
"""
string = input("Enter some words separated by a whitespace: ")
string_list = string.split(' ')
i = 0
for n in string_list:
    string_list[i] = n[::-1]
    i += 1
new_str = ' '.join(string_list)
print(new_str)
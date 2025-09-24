# List Methods
# Adding to the list: Insert(), Append(), Extend()
# Append only adds one argument
l1 = [1, 2.2, 'abc', 5]
print(l1)
# noinspection PyTypeChecker
l1.append([6, 7])
print(l1)

# list.extend()
# Extend Adds all the arguments but separately
l1.extend(['X', 'Y'])
print(l1)

# list.insert()
years = [2020, 2022, 2023]
years.insert(1, 2021)
print(years)
# Inserting on the last position
years.insert(len(years), 2024)
print(years)
years.insert(-1, 2025) # It adds a the argument to the second last position of the list
print(years)
years.clear() # Clears the arguments of the list

# list.pop() Removes the arguments one by one but it returns the argument where it can be stored in another variable
#If it has not been specified it removes the last argument
l2 = [10, 20, 30, 40]
x = l2.pop()
print(l2)
print(x)
y = l2.pop(1)
print(y, l2)

# list.remove()
# It searches for the value and when removed it cannot be returned
# It removes the first instance of the arguments
l3 = [10, 20, 30, 40, 20, 10, -1, 10, 16, 10]
l3.remove(20)
print(l3)
# To remove the all instances of an argument
while 10 in l3:
    l3.remove(10)

print(l3)

# List Index Part 2
print('#'*20 + 'LIST METHODS PART-2' + '#'*20)
# list.index()
names = ['John', 'tom', 'dan', 'john', 'bill']
i = names.index('tom')
print(f" Dan is at index {i}")
# list.count()
# It counts how many times an argument is in the list
letters = list('ahduwvauyvwtcwaiuawuiaaaiuabaaaibubdcbcgdsbcgusdb')
n = letters.count('a')
print(n)
# It is  not advices to use the in method it is advised to use the in operator
print('p' in letters)
print('a' in letters)
# list.reverse()
# It reverse the lists
b = letters.reverse()
print(b)
print(letters)
letters.reverse()
print(letters)

# Sorting Lists: list.sort() or sorted(list)
ages = [20, 30, 8, 23, 4, 16]
la = sorted(ages)
print(la)
grades = [80, 16, 20, 78, 19, 25, 30]
n = grades.sort()
print(n)
print(grades)




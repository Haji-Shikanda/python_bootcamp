l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(10)
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(id(l1), id(l2)) # The IDs of l1 and l2 are the same
l1.remove(2)
print(l2)
# Creating a copy
l3 = l1.copy()
l3.append('abc')
print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"l3: {l3}")

# 2.
nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2 ]
new_list = []
for n in nums:
    if n <=5:
        new_list.append(n) # The right way the loop saves the n<=5 to the new list
# List comprehension
my_list = [n for n in nums if n >= 5]
print(my_list)



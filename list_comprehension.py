# LIST COMPREHENSION
clicks = [10, 5, 15, 20]
double_list = list()
for c in clicks:
    double_list.append(c*2)
print(double_list)

# [expression for item in iterable]
double_numbers = [c*2 for c in clicks]
print(double_numbers)
name = 'ANDREI'
l1 = [char for char in name]
print(l1)
l2 = [char*2 for char in name]
print(l2)
l3 = [(char*3).lower() for char in name ]
print(l3)
nums = [1, 7, 8, 14, 21, 23, 50, 66, 70]
divisible_by_seven = [n for n in nums if n%7 == 0]
print(divisible_by_seven)
nums_str = [str(n) for n in nums ]
print(nums_str)
print('-'.join(nums_str))

friends = ['John', 'Mary', 'Dan']
neighbours = ['Tim', 'Steve', 'Dan', 'John']
friends_and_neighbours = [name for name in friends if name in neighbours ]
print(friends_and_neighbours)

family = ['Musa', 'ALI', 'TaNTa', 'Luffy']
members = ['LuFFy', 'Kassim', 'Rubi', 'Tanta']
family_lower = [n.lower() for n in family]
print(family_lower)
members_lower = [n.lower() for n in members]
print(members_lower)
family_and_members = [names for names in family_lower if names in members_lower]
print(family_and_members)
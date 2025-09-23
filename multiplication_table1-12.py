#Program to display multiplication of a given number
num = int(input("Enter a number: "))

for i in range(1,13):
    result = num * i
    print(f"{num} * {i} = {result}")
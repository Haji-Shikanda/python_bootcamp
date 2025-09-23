"""
Write a Python program that calculates and displays the sum,
the product and the average of n float numbers
entered by the user, each on a separate line. Enter 0 to finish.
"""
numbers = []
while True:
    num =float(input("Input the numbers (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("No number detected!!")
else:
    addition = sum(numbers)

    product = 1
    for n in numbers:
        product = product * n
    average = addition / len(numbers)

    print(f"The Sum = {addition}")
    print(f"The Product = {product}")
    print(f"The Average = {average}")



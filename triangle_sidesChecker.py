"""
Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
The user will be prompted for the triangle sides.
Note:
An equilateral triangle is a triangle in which all three sides have the same length.
An isosceles triangle is a triangle that has two equal si
"""
# Program to check the sides of a triangle
#Ask user for the 3 sides
sides = []
for i in range(1,4):
    side = int(input(f"Enter side {i} "))
    sides.append(side)

a, b, c = sides
if a == b == c:
     print("The Triangle is an Equilateral Triangle")
elif a==b or a==c or b==c:
     print("The Triangle is an Isosceles ")
else:
     print("The Triangle Scalene ")



"""
Consider the following string declaration which is part of the output of a Linux command.
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
Try to solve the challenge in more than one way.
"""
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
print(my_str.find('b4:6d:83:77:85:f3'))
mc_address = my_str.split()[-1]
print(mc_address)
r"""
Display the following strings literally:
It displayed: "You've got an error!"
\n means a new line.
\ is known as the escape character.
"""
print('It displayed: "You\'ve got an error!')
print("\\n means a new line.")
print(r"\ is known as escape character ")
"""
Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
The user will be prompted to enter the value in ft.
Display the value in cm with 2 decimals, formatted using an f-string.
"""
foot = float(input("Enter the value in foot(ft): "))
centimeters = foot * 30.48
print(f"The value in centimeters: {centimeters: .2f}cm")
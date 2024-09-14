# Conditions and Loops
"""
if elde loop:
`if condition:`
` // code you want to execute if the condition is true`
`else:`
`//  // code you want to execute if the condition is false`
"""
# Write a program to take a user age and let him know if he can go to the club
# 21
"""
Logic Building:
User input  - data type -> int
O/P - > string -> user if he can go or not

Rough Logic:
age > 21 -> print can go to the club
age < 21 -> print can't go

Write the logic:
"""

age = int(input("Enter Your age\n"))
if age > 21:
    print(f"Can go to the club with age - ", {age})
else:
    print(f"Can't go to the club with age - ", {age})

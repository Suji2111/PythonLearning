"""
 Create a program that takes two numbers as input and
 prints whether the first number is greater than, less than, or equal to the second number.
"""
num1 = int(input("Enter the value Num1: \n"))
num2 = int(input("Enter the value Num2: \n"))


if num1 > num2:
    print("The first number is greater than the second number")
elif num1 < num2:
    print("The first number is less than the second number")
else:
    print("The first number is equal to the second number")

"""
print("Number1 is greater than number2:",num1>num2)
print("Number1 is less than number2:",num1<num2)
print("Number1 is equal than number2:",num1==num2)
"""
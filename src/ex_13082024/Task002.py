"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

print("Max_Num of", num1, "and",num2, "is", max(num1, num2))
print("value of", num1, "to the power of", num2, "is:", pow(num1, num2))
print("Sum of", num1, "and", num2, "is", num1 + num2)
print("Sub of", num1, "and", num2, "is", num1 - num2)
print("Mul of", num1, "and", num2, "is", num1 * num2)
print("Div of", num1, "and", num2, "is", num1 / num2)

print("formatted_num1 is :", f"{num1 :.3f}")
print("formatted_num2 is :", f"{num2 :.3f}")
"""
- Explain the difference between the = operator and the == operator in Python.

- What does the ** operator do in Python, and how is it used?

- What does the ^ operator do in Python, and in what context is it commonly used?
"""
"""
In Python,  both the operators "=,==" serve different purposes and are used in different contexts:
# = Operator
Purpose: Assignment operator. It assigns the value to the variable on its left-hand side.
Context: This can be used to assign a value to the variable
Example: age = 34 -> Here, `34` is assigned to the variable `age`
         name = "Suji" -> Here, "Suji" is assigned to the variable `name`
# == Operator
Purpose: comparison operator. It checks whether the values on both sides are equal.
Context: This can be used to check if two values or expressions are equal, which returns a Boolean result (True or False).
Example:
a = 10
b = 20
print(a == b)  # Output: False, because `10` is not equal to `20`
c = 10
print(a == c)  # Output: True, because `10` is equal to `10`
"""

#In python ** operator is used for exponentation  (base**exponent)

a = int(input("Enter the value\n"))
b = int(input("Enter another value\n"))
print(a**b)

# In Python ^ operator is the bitwise XOR (exclusive OR)
"""
This operator performs a bitwise comparison between two integers, and it returns a new integer 
where each bit is set to 1 if the corresponding bits of the operands are different, and 0 if they are the same
"""
print(a^b)






# Data types & Identifiers

# Identifiers are names used to identify Variable, function, class, module or other objects
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# They start with a letter (A-Z or a-z) or an underscore (_) followed by zero or more letters, underscores, and digits (0-9).
# Python is case-sensitive, so myVariable and myvariable are two different identifiers.

a = 10
_ = 20
_ = _ + 1
print(_)
_abc = 123
# $123 = 11 - not allowed
# &123 = 12 - not allowed

pi = 3.14  # float
name = "Suji"  # str
age = 34  # int
isFemale = True  # bool
print(type(pi))
print(type(name))
print(type(age))
print(type(isFemale))

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)

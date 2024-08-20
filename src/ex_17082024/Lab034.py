# Ternary Operator
"""
if condition then do this
    else do that

if my_age > 18 then I can apply for voter Id
    else don't apply'

"""
#print("I will go to Goa" if int(input("Enter your age"))  > 18 else "can't go, stay home") - ternary operator

user_age = int(input("Enter your age"))

if user_age > 18:
    print("I will go to Goa")
else:
    print("Can't go, stay home")

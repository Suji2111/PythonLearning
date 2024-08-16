# Strings

name = "sujana"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a = "90"  # numerical values given in "" will be consider as string
A = 35
print(type(a))
print(type(A))

name = "This is a big line"
print(type(name))
# name = name+1 -- Not possible to add int to str
#name = name + "1"  # allowed
name = name + str(1) # allowed  -- Concatenation concept
print(name)

first_name = "Sujana"
last_name = ("chimily")
full_name = first_name + last_name
print(full_name)

Pets_I_Have = None
print(type(Pets_I_Have)) # NoneType -- datatype in Python

#Null is not present in Python

#id - function

age = 10
print(id(age)) # will give the memory
age2 = 10
print(id(age2)) # as the variable value is same both variable names will give same memory
"""
Write a Python program to calculate the area of a circle
given its radius using the formula  area=π×r^2 ( Take pie as 3.14)
"""
radius = float(input("Enter the radius\n"))
print(radius)

area = 3.14*pow(radius,2)
print(f"Area of circle whose radius is {radius: } =",area)



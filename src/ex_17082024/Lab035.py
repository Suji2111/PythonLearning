"""
Write a Python program to calculate the area of a circle
given its radius using the formula  area=π×r^2 ( Take pie as 3.14)
"""
#Logic buildng formula
# Step 1
"""
Figure out the inputs and outputs
input -> r -> data type -> float
pi -> 3.14
Power -> pow or ** -> any
O/p -> float - area, print area
"""
#Step 2
"""
rough Logic = area = 3.14 *pow(r,2)
"""
#Step 3 - write the logic
import math
radius = float(input("Enter the radius of the cirlce\n"))
print(radius)
area = math.pi*math.pow(radius, 2)
print("Area of the circle is", area)
print(f"Area of the circle is {area:.2f}")

#print(3.14*(float(input("Enter the radius\n"))**2))



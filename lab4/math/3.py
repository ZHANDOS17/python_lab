import math
from math import pi, tan
sides = int(input("number of sides: "))
length = int(input("the length of a side: "))
area = sides * (length**2)/(4*tan(pi / sides))
print("The area of the polygon is: ", round(area))
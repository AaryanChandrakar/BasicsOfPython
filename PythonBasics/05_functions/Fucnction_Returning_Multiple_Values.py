import math
def multiple_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = multiple_stats(3)
print("area of circle is",round(a,2),"and circumference is",round(c,2))
      
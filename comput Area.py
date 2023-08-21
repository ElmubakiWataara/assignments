import math
def areaOfCircle(radius):
    area = math.pi * radius **2
    return area
print(areaOfCircle(2))


def computeArea(b,d,w,h):
    area = w*h + 2*0.5 * b*d + w*d
    return area
print (computeArea(3,2,5,4))

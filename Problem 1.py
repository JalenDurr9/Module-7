Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def areaOfCircle(radius):
	return math.pi * radius ** 2

>>> r = float(input(" Please enter the radius of a circle: "))
 Please enter the radius of a circle: 15
>>> area = areaOfCircle(r)
>>> print(" Area Of a Circle = %.2f" %area)
 Area Of a Circle = 706.86
>>> 
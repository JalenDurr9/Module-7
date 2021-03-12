Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def rangeNumber(n):
	if int(num) in range(1, 10):
		print ("You entered a number in the range of 1 to 10")
	elif int(num) not in range(1, 10):
		print("Your number was not in the range")
	return

>>> num = int(input(" Enter a number:  "))
 Enter a number:  5
>>> val = rangeNumber(num)
You entered a number in the range of 1 to 10
>>> print(val)
None
>>> 
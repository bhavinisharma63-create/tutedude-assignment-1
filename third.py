Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #task 1
... 
... a = int(input('enter the number: '))
... print(a)
... def factorial(n):
...     if n == 0 or n == 1:
...         return 1
...     else:
...         return n * factorial(n - 1)
... result = factorial(a)
... print("The factorial of", a, "is", result)
... 
... # task 2
... 
... b=int(input('enter the number: '))
... from math import *
... print("square: ",sqrt(b))
... print("logarithm: ",log(b))

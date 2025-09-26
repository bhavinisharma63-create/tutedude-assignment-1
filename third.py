Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #task 1
... 
..def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
... 
... # task 2
... 
... num = float(input("Enter a number: "))
sqrt_val = math.sqrt(num)
log_val = math.log(num) 
sine_val = math.sin(num)      

print(f"Square root of {num}: {sqrt_val}")
print(f"Natural logarithm of {num}: {log_val}")
print(f"Sine of {num} (in radians): {sine_val}")

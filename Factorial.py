def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = 5

if num == 0:
    print("Factorial is:1")
elif num < 1:
    print("No negative numbers")
else:
    print(f"Factorial is {factorial(num)}")

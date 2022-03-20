# Fibonacci Series example
# 0,1,1,2,3,5,8,13,21,34,..........


def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))


count = 6

if count <= 0:
    print("Please enter value more than 2")
elif count <= 1:
    print("Please enter value more than 2")
else:
    for i in range(count):
        print(fib(i), end=" ")

# To print last value in Fibonacci series

if count <= 0:
    print("Please enter value more than 2")
elif count <= 1:
    print("Please enter value more than 2")
else:
    for i in range(count):
        lastValue = fib(i)
    print(lastValue)

# To print sum of Fibonacci series

if count <= 0:
    print("Please enter value more than 2")
elif count <= 1:
    print("Please enter value more than 2")
else:
    sumResult = 0
    for i in range(count):
        sumResult = sumResult + fib(i)
    print(sum)

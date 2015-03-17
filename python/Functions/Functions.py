def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


#print factorial(10)
#print fibonacci(4)
for x in range(0, 10):
    print fibonacci(x)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Don't divide by zero")
    else:
        return a/b

try:
    print divide(10, 2.0)
except ZeroDivisionError as e:
    print e
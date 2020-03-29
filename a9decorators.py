def repeater(oldFunction):
    def newFunction(*args, **kwds):
        oldFunction(*args, **kwds)
        oldFunction(*args, **kwds)
        oldFunction(*args, **kwds)
    return newFunction


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)

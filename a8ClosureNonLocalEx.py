# code here
def multiplierOf(x):
    def multiply(y):
        return x * y
    return multiply


multiplywith5 = multiplierOf(5)
print(multiplywith5(9))

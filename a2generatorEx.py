import random

def fib():
    a, b = 1, 1
    while 1:
        a, b = b, a + b
        yield a
    

import types
if type(fib()) == types.GeneratorType:
    print("the type of fib function is generator")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
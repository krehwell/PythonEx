# from functools import partial


# def multiply(x, y):
#     return x*y


# dbl = partial(multiply, 2)
# print(dbl(6))

# exercise to explore

from functools import partial


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# code below create and print with partial function
dbl = partial(func, 5, 5, 10)
print(dbl(5))

# partial wraps a function so that we only need to pass one value into it

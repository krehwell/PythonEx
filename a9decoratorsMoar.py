def prettySum(func):
    def inner(a, b):
        print(str(a)+" + "+str(b)+" is ", end="")
        return func(a, b)

    return inner


@prettySum
def sumAb(a, b):
    summed = a + b
    print(summed)


if __name__ == "__main__":
    sumAb(5, 3)

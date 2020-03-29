def typeCheck(correctType):
    # code here
    def check(oldfunction):
        def newFunction(arg):
            if (isinstance(arg, correctType)):
                return oldfunction(arg)
            else:
                return "bad type\n"
        return newFunction
    return check


@typeCheck(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2("not a number"))


@typeCheck(str)
def firstLetter(word):
    return word[0]


print(firstLetter("hello world"))
print(firstLetter(['not', 'a', 'string']))

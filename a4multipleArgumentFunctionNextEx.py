# functin here, use len(option) if we want to return the amount of extra argument
def foo(a, b, c, *option):
    b = 0
    for n in option:
        b = b + n
    return b


def bar(a, b, c, **option):
    if option.get("magicNumber") == 7:
        return True

    else:
        return False


# test code
if foo(1, 2, 3, 1) == 1:
    print("good.")

if foo(1, 2, 3, 1, 4) == 5:
    print("better.")

if bar(1, 2, 3, magicNumber=6) == False:
    print("great.")

if bar(1, 2, 3, magicNumber=7) == True:
    print("awesome!")

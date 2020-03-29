def who():
    print("Alice")


def display(func):
    def inner():
        print("the current user is : ", end="")
        func()
    return inner


@display
def name():
    print("Yuza")


if __name__ == "__main__":
    myobj = display(who)
    myobj()

    # this is a nice thing that function can take another function as
    # its argument
    # we can call it using other way that we put @ symbol above the
    # function and call it like this below
    name()

    # this is simpler that we dont have to assign another variable
    # as the example before this

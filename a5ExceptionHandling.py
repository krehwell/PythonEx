def doStuff(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            doStuff(the_list[i])
        except IndexError:  # raise when accesing a non existing index of a list
            doStuff(0)


catch_this()

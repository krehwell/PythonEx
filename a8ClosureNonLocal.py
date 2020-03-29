def printMsg(number):
    def printer():
        "here we are using the non local keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)


printMsg(9)

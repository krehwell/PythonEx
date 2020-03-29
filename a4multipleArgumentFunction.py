def myfunction(first, second, third, *theRest):
    print("first: %s" % first)
    print("second: %s" % second)
    print("third: %s" % third)
    print("and all the rest are... %s" % list(theRest))


myfunction(1, 2, 3, 4, 5, 6)

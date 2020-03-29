def doubleOut(oldFunction):
    def newFunction(*args, **kwds):
        return 2 * oldFunction(*args, **kwds)
    return newFunction


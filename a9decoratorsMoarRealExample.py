import time as t


def measureTime(func):
    def wrapper(*args):
        timeBuf = t.time()
        res = func(*args)
        print("the function took " + str(t.time() - timeBuf) +
              " second to run ")
        return res

    return wrapper


@measureTime
def myfunction(n):
    t.sleep(n)


if __name__ == "__main__":
    myfunction(2)

def transmitToSpace(message):
    "define the enclosing function"
    def printTheMessage():
        print(message)
    return printTheMessage


fun2 = transmitToSpace("burn the sun!")
fun2()

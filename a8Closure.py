def transmitToSpace(message):
    "this mis the enclosing function"
    def dataTransmitter():
        "the nested function"
        print(message)

    dataTransmitter()


print(transmitToSpace("test message"))

# setup
actor = {
    "name": "john cleese yuza",
    "rank": "awesome"
}

# function


def getLastName():
    name = actor.get("name")
    name = name.split()
    index = len(name)
    try:
        return name[index]

    except IndexError:
        index -= 1
        return name[index]


# test code
getLastName()
print("all exception caought! good job!")
print("the actor's last name is %s" % getLastName())

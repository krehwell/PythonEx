# help()
# dir()
# hasattr()
# id()
# type()
# repr()
# callable()
# issubclass()
# isinstance()

# ex
# define a class vehicle


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % \
            (self.name, self.color, self.kind, self.value)
        return desc_str


# print this to see whats inside the vehicle class
# print(dir(Vehicle))
v = Vehicle()
v.name = "mercy"
v.color = "black"
print(v.description())

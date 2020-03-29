class myClass:
    variable = "blah"

    def function(self):
        print("this is a masssage inside the class.")

myobjectx = myClass()
myobjecty = myClass()
myobjecty.variable = "yuza"
print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()
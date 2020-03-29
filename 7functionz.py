#define the functino
def my_function():
    print("hello my good friend")

def my_functionWithArgument(name, age):
    print("calling from function, name is %s, %s years old" % (name, age))

def my_functionReturn(num1, num2):
    return num1 * num2

my_function()
my_functionWithArgument("yuza", 23)
print("the return value of function is %d" %my_functionReturn(3,4))
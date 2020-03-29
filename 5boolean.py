name = "john"
age = 23

if name == "john" and age == 23:
    print("your name is johnk, 23 years old")

if name == "john" or name == "rick":
    print("hello not rick")


if name in ["john", "rick"]:
    pass #variable to say you want to do nothing
elif age == 23:
    print("jon you are 23?")


# comparing from memory adress
a = [1,2,3]
b = a
c = [1,2,3]

print(a is c)
print(a is b)
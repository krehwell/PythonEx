def bar(first, second, third, **option):
    print(list(option))
    if option.get("action") == "sum":
        print("the sum is: %d" % (first + second + third))

    if option.get("number") == "first":
        return first


# send the argument with name action and number
result = bar(1, 2, 3, action="sum", number="first")
print("Result is: %d" % (result))

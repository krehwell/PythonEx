print(set("my name is eric and eric is my name".split()))

a = set(["jake", "john", "eric"])
b = set(["john", "jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

# exercise. use the given list to pritn set containing all the participant
# from A which did not attend event B

print(a.difference(b))

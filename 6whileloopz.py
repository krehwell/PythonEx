count = 0
while count < 5:
    print(count, end= " ")
    count += 1
print()

#using break to stop
count = 0
while True:
    print(count, end=" ")
    count +=1
    if count >= 7:
        break
print()

#using range
for x in range(10):
    if x % 2 == 0:
        continue
    print(x, end=" ")


#using else for while, what a gay 
i = 0
while (i < 5):
    print(i)
    i = i + 1
else:
    print("count is stop at: %d" % i)


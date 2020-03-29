import random

def lottery():
    #return  6 number from 1 and 40
    for i in range(6):
        yield random.randint(35, 40)
        
    yield random.randint(1,10)

for random_number in lottery():
    print("and the next number is... %d" % (random_number))
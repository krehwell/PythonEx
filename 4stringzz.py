astring = "Hello worlD"

#print the length of the string
print("a single quote string ' ' ")
print(len(astring))

#PRINT the number of index 
print("the o is occur at %d index" % astring.index("o"))

#PRINT the number of occurance
print("the letter l occur %s times" % astring.count("l"))

#print from start to end given length
print(astring[3:15])
print(astring[0:7:2]) #skipping 2 character front, -2 for the back skip 

#print reverse
print(astring[::-1])

#capitalize and non capp
print(astring.upper())
print(astring.lower())

#get the value true or false base on the given
print(astring.startswith("Hell"))
print(astring.endswith("Worldzz"))

#the way to split into becoming word by word
a = astring
b = astring.split(" ")
print(a[1])
print(b[0])
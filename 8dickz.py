phonebook = {}
phonebook["john"] = 420
phonebook["jack"] = 69
phonebook["jill"] = 13

#another way to initialize
phonebook = {
    "john": 13,
    "jack": 420,
    "jill": 69
}
print(phonebook)

#how to iterate it
string = "%s favorite number is %d"
for name, x in phonebook.items():
    print(string % (name, x))

#removing the value
sexPhonebook = {
    "yuza": 69,
    "teti": 420,
    "ras": 13
}
del sexPhonebook["ras"]
#or
del sexPhonebook["teti"]
print(sexPhonebook)
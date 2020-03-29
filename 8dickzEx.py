phonebook = {
    "john": 13,
    "wick": 420,
    "teti": 69
}

#code here removeing teti and add jill as the replacement
phonebook["jake"] = 22
del phonebook["teti"]
print(phonebook)

if "jake" in phonebook:
    print("jake is in phonebook")
if "teti" not in phonebook:
    print("teti is not in the phonebook")
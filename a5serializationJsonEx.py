import json


def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    print(salaries)
    salaries[name] = salary
    salaries["hell"] = 10
    print(salaries)
    return json.dumps(salaries)


# test code
salaries = '{"alfred" : 300, "jane" : 300}'
new_salaries = add_employee(salaries, "me", 800)
decode_salaries = json.loads(new_salaries)
print(decode_salaries["alfred"])
print(decode_salaries["jane"])
print(decode_salaries["me"])

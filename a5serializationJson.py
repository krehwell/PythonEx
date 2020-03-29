import pickle
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(json.loads(json_string))

# or using pickle

pickle_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickle_string))

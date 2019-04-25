import json

with open('/home/rojanshrestha/Desktop/pythonmjml/sampletestjson.json', 'r') as f:
    json_text = f.read()

# Decode the JSON string into a Python dictionary.
a_dict = json.loads(json_text)
print(a_dict)


with open('hello.txt', 'w') as json_file:
  json.dump(a_dict, json_file, indent = 4, sort_keys=True)

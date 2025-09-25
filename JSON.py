# Converting Python → JSON (Serialization / Dumping)
import json

data = {"name": "Ali", "age": 20, "city": "Karachi"}
json_string = json.dumps(data)
print(json_string)


# Converting JSON → Python (Deserialization / Loading)
import json

json_data = '{"name": "Sara", "age": 22, "city": "Lahore"}'
python_dict = json.loads(json_data)
print(python_dict["name"])


# Writing JSON to a File
import json

data = {"course": "Python", "level": "Beginner"}

with open("data.json", "w") as f:
    json.dump(data, f)
    

# Reading JSON from a File
import json

with open("data.json", "r") as f:
    content = json.load(f)
    print(content)
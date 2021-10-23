import json

# some JSON:

x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary:
print(y["age"])


# converting python to JSON
# python dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# convert into json
y = json.dumps(x)

# results
print(y)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964
}

print(thisdict)
print(thisdict["brand"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020
}

print(thisdict)

# length of dictionary
print(len(thisdict))

# type
print(type(thisdict))

# using get
x = thisdict.get("model")

print(x)

# get keys
x = thisdict.keys()

print(x)

# adding items

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before change

car["color"] = "white"

print(x)  # after change

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

x = car.items()

print(x)

# checking if model exist
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# updating dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"year": 2020})

print(thisdict)

# adding items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"color": "red"})

print(thisdict)

# remove item from dictionary by popping
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")
print(thisdict)

del thisdict["year"]
print(thisdict)

# clear () will empty the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)

# looping through the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# all key names
for x in thisdict:
    print(x)

# print all values
for x in thisdict:
    print(thisdict[x])

# print all values 2
for x in thisdict.values():
    print(x)

# another way of doing the keys
for x in thisdict.keys():
    print(x)

# looping through both keys and values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x, y in thisdict.items():
    print(x, y)

# copying a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()
print(mydict)

# copy 2
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = dict(thisdict)
print(mydict)

# multiple dictionaries

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)

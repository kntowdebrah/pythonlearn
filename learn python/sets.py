#length of a set
thisset = {"apple","banana","cherry"}
print(len(thisset))

#various data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

myset = {"apple", "banana", "cherry"}
print(type(myset))

#set constructor
thisset =set(("apple", "banana", "cherry"))
print(thisset)

#accessing items in a set1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#check if banana is in the set
print("banana" in thisset)

#adding items to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print (thisset)

#adding one set to another using update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#updating a set by any other iterable object(list, tuples, dictionaries)
citiesOfTheWorld = {"London","Amsterdam","Paris", "Washington DC"}

citiesOfAfrica = ("Accra", "Lagos", "Abidjan")

citiesOfTheWorld.update(citiesOfAfrica)

print(citiesOfTheWorld)

x = citiesOfTheWorld.pop()

#citiesOfAfrica.clear()

print(citiesOfAfrica)

print(x)

#looping through a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#joing two sets use

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print (set3)

#updates
set1.update(set2)
print (set1)

#intersect
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print (x)

#symmetric_difference_update()
x.symmetric_difference_update(y)
print (x)

#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

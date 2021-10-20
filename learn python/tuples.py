#tuples
thistuple = ("apple","banana", "cherry")

print(thistuple)
print(len(thistuple))

thistuple =("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

#using the tuple constructor
thistuple = tuple(("apple","banana","cherry"))
print(thistuple)

#accessing tuples
thistuple = ("apple","banana","cherry")
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[-4:-1])

#check if item exists
thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#neat trick with tuples
x = ("apple","banana","cherry")
y = list(x)

#replace
y[1] = "kiwi"
x = tuple(y)

#adding items to the tuples
cities = ("Accra","New York","Lome","Worcester")

citieslist = list(cities)

citieslist.append("Kumasi")

cities = tuple(citieslist)

print(cities)

#adding using another tuples
cities = ("Accra","New York","Lome","Worcester")
city = ("Boston",)

cities+=city

print(cities)

#deleting a tuple
#del cities
#print(cities)

#upacking a tuples
fruits = ("apple", "banana", "cherry")

(green, red, blue) = fruits

print(green)
print(red)
print(blue)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#looping through a tuples
thistuple =("apple", "banana","cherry")
for x in thistuple:
    print(x)

#looping through using the index
thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(thistuple[i])

#looping using a while loop
thistuple = ("apple","banana","cherry")
i = 0

while i < len(thistuple):
    print(thistuple[i])
    i=i+1

#joining two tuples
tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

#muliplying tuple
fruit = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print("")
print("")
print("")

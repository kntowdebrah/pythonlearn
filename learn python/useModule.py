
from mymodule import person1
import platform
import mymodule as mx

#mymodule.greeting("Hello testing out module")

a = mx.person1["age"]
print(a)

x = platform.system()

print(x)

x = dir(platform)
print(x)

# importing only the dictionary

print(person1["age"])

# lambda
def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))

# lambda functions


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))

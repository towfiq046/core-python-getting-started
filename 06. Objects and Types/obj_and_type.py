# CORE RULE: Assignment operator only binds objects to names it never copies objects by value.

x = 1000
# Here int object is created with value 1000.
# x is also an object.
# object x refers to the int object 1000.
# Like this x -> int 1000

x = 500
# Here int object 1000 isn't changed.
# int object is IMMUTABLE in python.
# Redirects the x reference to point to the the new int object 500.

# Now int object 1000 is not reachable and python garbage collector will reclaim it at some point.

y = x
# When we assign one variable to another we are really assigning one object reference to another object reference.
# Like this x -> int 500 <- y

# id()
a = 10
print(id(a))
b = 20
print(id(b))

b = a
print(id(b))
print(id(a) == id(b))
print(a is b)
print('\n')


t = 5
print('id of initial t:')
print(id(t))
t += 1  # += augmented assignment operator.
print('id of current t:')
print(id(t))
print('\n')
# int object is not mutating.

# Example with mutable object, list.
i = [1, 2, 3]
s = i
s[1] = 5

print('assigning one list to another')
print(i, s)
print(s is i)
print('\n')


k = [4, 3, 9]
l = [4, 3, 9]

print(k == l)
print(k is l)

# Value equality and identity equality are different.
# Value comparison can be controlled programmatically.
# Identity comparison is defined by the language and can't be altered.

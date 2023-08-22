# A Tuple is exactly same as a List, except that its immutable.

myTuple = ("Max", 28, "Boston")
print(myTuple)
print(type(myTuple))

# The paranthesis is optional
myTuple = "Max", 28, "Boston"
print(myTuple)
print(type(myTuple))

# Right way to declare a tuple with single element
# Wrong way:
a_Tuple = ("Max")
print(type(a_Tuple))

# Right way:
a_Tuple = ("Max",)
print(type(a_Tuple))

# Tuple constructor of 'tuple' class
myTuple = tuple(["Sham", 30, "Pune"])
print(myTuple[0], ' is ', myTuple[1], ' years old and he lives in ', myTuple[2])

# We cannot modify the tuple by any mean
# myTuple[0] = "Kartik"
# The above line will generate error


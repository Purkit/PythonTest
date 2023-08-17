# Encapsulation in Python !

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value
    
    @staticmethod
    def some_static_method():
        print("\nHello World")


Person.some_static_method()

p1 = Person("Kartik", 23, 'm')
print(p1.Name)

# We can't do: p1.__name

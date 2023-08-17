# Proxy Design Pattern

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ An Abstract Interface Method """
        pass

class Student(IPerson):
    """ WE WILL NOT DEFINE A CONSTRUCTOR HERE"""
    
    def person_method(self):
        print('I am a student')

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Student()
    
    def person_method():
        print("I'm the proxy funtionality")
        self.person.person_method()

p1 = Student()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
# Factory Design Pattern

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ An Abstract Interface Method """
        pass



class Student(IPerson):
    def __init__(self):
        self.name = "Default_Student"
    
    def person_method(self):
        print('I am a student')

class Teacher(IPerson):
    def __init__(self):
        self.name = "Default_Teacher"
    
    def person_method(self):
        print('I am a Teacher')


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print('Invalid Type')
        return -1


if __name__ == "__main__":
    choice = input("What type of person you want to create ?\n")
    desired_person = PersonFactory.build_person(choice)
    desired_person.person_method()
# Singelton Designe Pattern

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def print_data():
        """Implement in child class"""


class PersonSingenton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingenton.__instance == None:
            PersonSingenton("Default", 0)
        return PersonSingenton.__instance
    
    def __init__(self, name, age):
        if PersonSingenton.__instance != None:
            raise Exception("Singenton class cannot be instantiated multiple time !")
        else:
            self.name = name
            self.age = age
            PersonSingenton.__instance = self
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingenton.__instance.name} , Age: {PersonSingenton.__instance.age}")

the_king = PersonSingenton("Kartik", 50)
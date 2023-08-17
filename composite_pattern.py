# Composite Design Pattern

from abc import ABCMeta, abstractstaticmethod

class IDepartment():
    @abstractstaticmethod
    def __init__(self, employes):
        """implement in child class"""
    
    @abstractstaticmethod
    def print_detartment():
        """implement in child class"""

class Accounting(IDepartment):
    def __init__(self, employes):
        self.employes = employes
    
    def print_detartment(self):
        print(f"Accounting Department: {self.employes}")

class Development(IDepartment):
    def __init__(self, employes):
        self.employes = employes
    
    def print_detartment(self):
        print(f"Development Department: {self.employes}")


class ParentDepartment(IDepartment):
    def __init__(self, employes):
        self.employes = employes
        self.base_empolyes = employes
        self.sub_departments = []
    
    def add(self, department):
        self.sub_departments.append(department)
        self.employes += department.employes
    
    def print_detartment(self):
        print("Parent Department")
        print(f"Parent Department Base Employes: {self.base_empolyes}")
        for department in self.sub_departments:
            department.print_detartment()
        print(f"Total No. of Employes: {self.employes}")

department_1 = Accounting(700)
department_2 = Development(300)

administrative_department = ParentDepartment(30)
administrative_department.add(department_1)
administrative_department.add(department_2)

administrative_department.print_detartment()
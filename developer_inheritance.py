# Create a Developer class that inherits from both Person and Employee and adds a programming_language attribute.

class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id


class Developer(Person, Employee):
    def __init__(self, name, emp_id, programming_language):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.programming_language = programming_language

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Language: {self.programming_language}")


dev = Developer("Safdar", "E101", "Python")
dev.display_details()


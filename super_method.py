# Use super() in a subclass to extend a method.

class Parent:
    def introduce(self):
        print("Hello from Parent!")


class Child(Parent):
    def introduce(self):
        super().introduce()  
        print("Hello from Child!")


c = Child()
c.introduce()


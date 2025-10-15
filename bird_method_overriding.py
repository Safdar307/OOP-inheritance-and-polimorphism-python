# Create a Bird class inheriting from Animal and override eat(). Add a fly() method.

class Animal:
    def eat(self):
        print("The animal is eating.")


class Bird(Animal):
    def eat(self):
        print("The bird is pecking grains.")

    def fly(self):
        print("The bird is flying high in the sky.")


b = Bird()
b.eat()
b.fly()

# Implement multiple inheritance: Create Amphibian inheriting from Swimmer and Walker (define Walker with a walk() method).


class Swimmer:
    def swim(self):
        print("Swim in water.")


class Walker:
    def walk(self):
        print("Walking on land.")


class Amphibian(Swimmer, Walker):
    def show_ability(self):
        print("Amphibians can both walk and swim.")

a = Amphibian()
a.walk()
a.swim()
a.show_ability()

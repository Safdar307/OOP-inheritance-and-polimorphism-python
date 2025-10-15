# Create a Motorcycle class that inherits from Vehicle and adds a has_sidecar attribute.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar ):
        
        super().__init__(brand, model, year)
        
        self.has_sidecar = has_sidecar

    def show_details(self):
        super().show_details()
        print(f"Has Sidecar: {'Yes' if self.has_sidecar else 'No'}")

bike1 = Motorcycle("Honda", "CD 70", 2025, False )
bike2 = Motorcycle("Express", "Unknown", 2024, True)

bike1.show_details()
print()
bike2.show_details()



      
        
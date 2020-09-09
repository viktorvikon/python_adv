class CarBase:

    def __init__(self, brand, speed, tires):
        self.brand = brand
        self.speed = speed
        self.tires = tires
    
    def __str__(self):
        return f"'{self.brand}' mooves using {self.tires} with {self.speed} km/h."
        

class Car(CarBase):

    def __init__(self, brand, speed, tires, seats_count):
        super().__init__(brand, speed, tires)
        self.seats_count = seats_count

    def __str__(self):
        main_str = super().__str__()
        nem_str = f"The car {main_str}\nThe passenger seat count =  {self.seats_count}" 
        return nem_str


class Truck(CarBase):

    def __init__(self, brand, speed, tires, сargo_volume):
        super().__init__(brand, speed, tires)
        self.сargo_volume = float(сargo_volume)

    def __str__(self):
        main_str = super().__str__()
        nem_str = f"The truck {main_str}\nThe сargo volume =  {self.сargo_volume} ton / tons" 
        return nem_str


print("-" * 45)
seat = Car("Seat", 100, "winter tires", 5)
print(seat)
print("-" * 45)
man = Truck("Man", 70, "winter tires", 1.5)
print(man)
print("-" * 45)

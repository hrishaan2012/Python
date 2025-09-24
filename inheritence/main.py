class vehical():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehical):
    def __init__(self, name, max_speed, mileage, capacity, brand):
        self.capacity = capacity
        self.brand = brand
        vehical.__init__(self, name, max_speed, mileage)

School_bus = bus("School Volvo", 180, 12, 50, "Volvo")
print("Vehical name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage, "Capacity:", School_bus.capacity, "Brand:", School_bus.brand)
        
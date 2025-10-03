class Transport:
    def __init__(self, title, avg_mileage, seats):
        self.title = title
        self.avg_mileage = avg_mileage
        self.seats = seats

    def cost(self):
        return self.seats * 100


class Shuttle(Transport):
    def cost(self):
        base_cost = super().cost()
        base_cost += base_cost * 10 / 100
        return base_cost


city_bus = Shuttle("City Shuttle", 15, 60)
print("Total Shuttle Fare is:", city_bus.cost())

class bird:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
blu=bird("Parrot",15)
woo=bird("Parrot",20)
print(f"blu is a {(blu.species)}")
print(f"woo is also a {(woo.species)}")
 
class dogs:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

#Object creation
Dog1 = dogs("Spike", 3, "Bulldog")
Dog2 = dogs("Kitty", 1, "Pitbull")

print(Dog1.name, Dog1.age, Dog1.breed)
print(Dog2.name, Dog2.age, Dog2.breed)
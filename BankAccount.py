#OOP -Classes - Blueprints for objects
class Animal:
    #name
    #age
    #species

#add dynamic attributes for properties
    def __init__(self, name, age, species):
        self.name = name 
        self.age = age
        self.species = species

rose = Animal("Rose", 5, "Dog")
sparky = Animal("Sparky", 3, "Cat")
print(rose)


print(rose.name)
print(rose.age)
print(rose.species)

print(sparky)
print(sparky.name)
print(sparky.age)
print(sparky.species)
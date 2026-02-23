#Name: Nailah Wanjiku
#Date: 23/2/2026
#Program to show inheritance in python

class Animal():
    def__init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} in kgs")

    def eat(self,food):
        print(f"The animal eats the {food}")




class Dog(Animal):
    def__init__(self, color, height, breed):
        super().__init__(species, weight, food)
        self.color = color
        self.height = height
        self.breed = breed

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The dog weighs {weight} in kgs")

    def barks(self):
        print(f"The dog says woof woof")




class Horse(Animal):
    def__init__(self, color, height, breed):
        self.color = color
        self.weight = weight
        self.breed = breed

    def (self,weight):
        weight = 1.1 * weight
        print(f"The dog weighs {weight} in kgs")

    def neighs(self):
        print(f"The horse says neigh neigh")







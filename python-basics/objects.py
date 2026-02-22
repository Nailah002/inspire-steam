#Name: Nailah Wanjiku
#Date: 19/2/2026
#Program to show objects

class Human:
    #First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city ="Nairobi"

    #We then create a constructor for the class object
    #The constructor will be used to create copies of this object
    def__init__(self,name,age): 
       self.human_name = name
       self.human_age = age

    def tell_story(self):
        print(f"Hello, i am {self.name} here is a story")
        print(f"There was once a man named Isaac Newton")

#Create the humans
sophy = Human("sophy:",20)
elvis = Human("elvis:",16)

#Let humans created do things
sophy.tell_story()
print("sophy's age is:", sophy.human_age)

#Modify one of the objects without modifying other objects
elvis.city = "Kiambu"

print("elvis's location:",elvis.city)
print("sophy's location:",sophy.city)


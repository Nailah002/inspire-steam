#Name: Nailah Wanjiku
#Date: 19/2/2026
#Program to display functions


def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2

    print(f"The pan is {pan}, and the fire is {fire},\ add {oil} amount of oil and cook {eggs} eggs")

print("Here is statement 1")
print("Here is statement 2")

cook_egg()

print("Here is staement 3")

#Ride fare creating function

def create_fare(route, distance, rush_hour):
    fare = distance * 10
    if rush_hour == True:
        fare = fare * 1.5
    print(f"Your fare to {route} is {fare}")

rush_hour = True
returned_fare = create_fare("Juja-Allsops",7,rush_hour)

print(f"The fare returned is: {returned_fare}")
create_fare("Juja-Allsops",7,rush_hour)

#passing a list as a parameter
def write_all_interests(interests):
    for interests in interests:
        print(f"I am interested in {interests}")

all_interests = ["watching videos","playing games","reading"]

write_all_interests(all_interests)
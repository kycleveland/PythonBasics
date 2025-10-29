from classes.my_classes import Car

# Creating the data for the cars
my_car = Car(make="Nissan", model="Titan SV", year=2021, mileage=92000, condition="Above Average", color="White")
my_wifes_car = Car(make="Nissan", model="Rogue SL", year=2023, mileage=52000, condition="Great", color="White")

# print(my_car.make)
# print(my_wifes_car.__dict__)

my_car.start()
my_car.accelerate(20)
my_car.accelerate(30)
my_car.stop()
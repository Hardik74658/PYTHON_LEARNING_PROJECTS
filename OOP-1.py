class Car:
    seating_capacity = 5        # class variable
    allCars = []

    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
        Car.allCars.append(self)

    # creating a method
    @classmethod
    def addNew(cls, name, price, fuel):
        return cls(name, price, fuel)

    def displayDetails(self):
        print("---------- Details of c1 ----------")
        print("Model Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()

    def showAllCars():
        print("Sr.No. \t Name")
        index = 0
        for car in Car.allCars:
            print(f"{index}\t{car.name}")
            index += 1

    def changeDetails(self):
        print("Enter new details (Press Enter If Want Same Detail):")
        name = input("Name: ")
        self.name = self.name if name == "" else name
        price = input("Price: ")
        self.price = self.price if price == "" else price
        fuel = input("Fuel: ")
        self.fuel = self.fuel if fuel == "" else fuel

    @staticmethod
    def deleteCar():
        Car.allCars.pop(car)
    # def displayDetails(self, something):
    #     print("Something is -", something)


c1 = Car("Elantra", 2500000, "Petrol")
# c1.displayDetails("Nothing")

c2 = Car("Verna", 1200000, "Petrol")
# c1.changeDetails()
# c1.displayDetails()
c3 = Car("Fortuner", 3500000, "Diesel")

"""Press 1 - to add a new car
2 - display details of an existing car
3 - change details of an existing car
4 - delete a car
5 - exit
"""
# Your code goes here
# Car.showAllCars()
while True:
    print("Press 1 - to add a new car")
    print("Press 2 - display details of an existing car")
    print("Press 3 - change details of an existing car")
    print("Press 4 - delete a car")
    print("Press 5 - exit")
    choice = int(input())

    if choice == 1:
        Car.addNew(input("Enter Car Name : "), input(
            "Enter Car Price : "), input("Enter Car Fuel Type : "))
    elif choice == 2:
        Car.showAllCars()
        car = int(input("Enter Car Index : "))
        Car.allCars[car].displayDetails()

    elif choice == 3:
        Car.showAllCars()
        car = int(input("Enter Car Index : "))
        Car.allCars[car].changeDetails()
    elif choice == 4:
        Car.showAllCars()
        car = int(input("Enter Car Index : "))
        Car.deleteCar()
    elif choice == 5:
        break
    else:
        print("Invalid Choice!!")

# Marcos Valenica
# SDEV 220
# 11/14/2022
# This code is to accept user input for a vehicle type and the information of the vehicle entered by the user. Then display it for the user

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self,type,year,make,model,doors,roof):
        self.type = type
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof

type2=input("Type of vehicle: ")
year2=input("Enter the Year: ")
make2=input("Enter the manufacture: ")
model2=input("Enter the model: ")
doors2=input("Enter number of doors: ")
roof2=input("solid or sun roof: ")
X=Automobile(type2,year2,make2,model2,doors2,roof2)
print("\n Vehicle Type: "+X.type)
print("\nYear: "+X.year)
print("\nMake: "+X.make)
print("\nModel: "+X.model)
print("\nDoors: "+X.doors)
print("\nRoof Type: "+X.roof)
"""
Class is a blue print
"""

class Car:
    # similar to constructor concept
    # self keyword references to instance of the class
    def __init__(self, brand: str, color: str, horsepower: int) -> None:
        self.brand = brand
        self.color = color
        self.horsepower = horsepower


    # method
    def drive(self) -> None:
        print(f'{self.brand} is driving')

alto: Car = Car('Maruthi Suzuki Alto','Grey', 2500)
volkswagen: Car = Car('Volkswagen','Red', 4800)
ferrari: Car = Car('Ferrari','White', 9800)
print('Alto')
print('-------------------------------------------')
alto.drive()
print('Color: ', alto.color,'Horsepower: ', alto.horsepower)
print('-------------------------------------------')
print('Volkswagen')
print('-------------------------------------------')
volkswagen.drive()
print('Color: ',volkswagen.color,'Horsepower: ', volkswagen.horsepower)
print('-------------------------------------------')
print('Ferrari')
print('-------------------------------------------')
ferrari.drive()
print('Color: ',ferrari.color,'Horsepower: ', ferrari.horsepower)
print('-------------------------------------------')


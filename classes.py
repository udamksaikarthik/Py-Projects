"""
Class is a blue print
"""

from typing import Self


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

    # dunder methods
    def __str__(self) -> str:
        return f'{self.brand} is driving with horsepower {self.horsepower}, which is of {self.color} color.'
    
    def __add__(self, other1: Self) -> str:
        return f'{self.brand} & {other1.brand}'

alto: Car = Car('Maruthi Suzuki Alto','Grey', 2500)
volkswagen: Car = Car('Volkswagen','Red', 4800)
ferrari: Car = Car('Ferrari','White', 9800)
print('Alto')
print('-------------------------------------------')
alto.drive()
print('Color: ', alto.color,'Horsepower: ', alto.horsepower)
print(alto) # instead of returning the object, this will call dunder method of __str__
print('-------------------------------------------')
print('Volkswagen')
print('-------------------------------------------')
volkswagen.drive()
print('Color: ',volkswagen.color,'Horsepower: ', volkswagen.horsepower)
print(volkswagen) # instead of returning the object, this will call dunder method of __str__
print('-------------------------------------------')
print('Ferrari')
print('-------------------------------------------')
ferrari.drive()
print('Color: ',ferrari.color,'Horsepower: ', ferrari.horsepower)
print(ferrari) # instead of returning the object, this will call dunder method of __str__
print('-------------------------------------------')

print(alto + volkswagen)


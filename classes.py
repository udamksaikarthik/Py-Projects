"""
Class is a blue print
"""

class Car:
    # similar to constructor concept
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower

alto: Car = Car('Grey', 2500)
volkswagen: Car = Car('Red', 4800)
ferrari: Car = Car('White', 9800)
print('Alto')
print('-------------------------------------------')
print('Color: ', alto.color,'Horsepower: ', alto.horsepower)
print('-------------------------------------------')
print('Volkswagen')
print('-------------------------------------------')
print('Color: ',volkswagen.color,'Horsepower: ', volkswagen.horsepower)
print('-------------------------------------------')
print('Ferrari')
print('-------------------------------------------')
print('Color: ',ferrari.color,'Horsepower: ', ferrari.horsepower)
print('-------------------------------------------')


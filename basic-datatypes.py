# datatypes
# type annotation format as below
from typing import Final
from datetime import datetime
from functions import showtime, showtimereturn


number: int = 10
decimal: float = 1.5
name: str = "Karthik!"
active: bool = False

#Constant variable
VERSION: Final[str] = '1.0.4'


print('VERSION: ',VERSION)

# this is not working as expected, we will cover this in functions.
VERSION = '2.0.6'

print('VERSION: ',VERSION)


# list is a collection of different data types
names: list = ['Karthik', 'Gayathri', 'Rudhvedh',21, 20, 18] 
# tuples are similar to lists, but tuples are immutable and once declared can't be changed
coordinates: tuple = (1.5, 1.5, 2.5)
# Set is similat to lists as well, but can't have duplicates. (unique)
unique: set = {1, 2, 2, 4, 9}
# key value pair system.
data: dict = {'name': 'Karthik', 'age': 26}

print('names: ',names)
print('coordinates: ',coordinates)
print('unique: ',unique)
print('data: ',data)

print('datetime:', end=" ")

showtime()

print('datetime:', showtimereturn())
from datetime import datetime

# function to show datetime
"""
this function return nothing(like void function)
prints the current date and time
"""
def showtime() -> None:
    print(datetime.now())

"""
this function return datetime
returns the current date and time
"""
def showtimereturn() -> datetime:
    return datetime.now()

"""
this function has parameter 
Parameterized function
"""
def greet(name: str) -> None:
    print('Hello, ',name,"!!")

greet('Karthik')
greet('Gayathri')

"""
this function has parameter 
Parameterized function
"""
def greet(name: str) -> None:
    print('Hello, ',name,"!!")

"""
this function has parameter 
Parameterized function to add numbers
"""
def add(a: float, b: float) -> float:
    return a + b

print('add: ',add(1.5, 5.9))
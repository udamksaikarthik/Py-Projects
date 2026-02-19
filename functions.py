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


"""
this function has accepting multiple parameters 
Parameterized function to add numbers
"""
def add(a: int, *b: int) -> int:
    sum = a
    for n in b:
        sum += n
    
    return sum

print(add(4,5,5,5,5,5,5,5,5))

"""
anonymous function: which is without a name

"""

# def fun(num: int) -> int:
#     return num * num

fun = lambda num: num * num

result = fun(5)
print(result)

add_anon = lambda a,b: a+b


result = add_anon(5, 5)
print(result)
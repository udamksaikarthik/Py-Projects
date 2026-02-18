import sys
from time import sleep
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

count = 1

# function calling itself is called recursion
def greet():
    global count
    print('Hello!', count)
    count = count + 1
    sleep(0.01)
    greet()

greet()
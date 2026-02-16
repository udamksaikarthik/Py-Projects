#imports
import sys

#print statements...
print(sys.version)

print('Hello world')
print("I am learning python")
print('It is awesome', end=" ")
print('and fun')

"""
This is a comment
written in more
than one line...
"""

#variables
number = 9

#casting to specify a data type

x = str(3)
y = int(3)
z = float(3)

print('x: ',x, ', y: ',y,',z: ',z)
print('typeof x: ',type(x), ', typeof y: ',type(y),', typeof z: ',type(z))

#if else condition
if(number%2==0):
    print(number, "is a even number")
else:
    print(number, " is a odd number")


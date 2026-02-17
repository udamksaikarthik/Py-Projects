from array import *

# Arrays

arr1 = array('f',[2.5, 4.8, -3.2, 6.7]) #accepts the float type only

arr1.append(77.7)

arr1.reverse()


for i in arr1:
    if i < 0:
        continue
    print(i)


# arr2 = array(arr1.typecode , arr1.tolist())

arr2 = array(arr1.typecode , (n for n in arr1))

arr1[2] = 3.4

print(arr1)
print(arr2)

# user defined array

size = input('Enter the size of array: ')

size = int(size)

arrayUser = array('i')

for n in range(size):
    value = input(f'Enter the {n} position value for array: ')
    arrayUser.append(int(value))

print(arrayUser)


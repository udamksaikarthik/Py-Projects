age = input('Enter your age:')

age = int(age)

if age>=18:
    print('you are Eligible to vote.')
else:
    print('You are not eligible to vote yet, because ur age is less than 18')


# Nested If

num = int(age)

if num > 5:
    if num > 9:
        print(f"{num} is greater than 5 and 9")
    else:
        print(f"{num} is less than 9 and greater than 5")
else:
    print(f'{num} is less than 5')

# match (similar to switch from other languages)

match num:
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
    case _:
        print('someother number')
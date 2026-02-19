from functools import reduce

nums = [2, 3, 4, 5, 6, 7, 8, 9 ,10]

evens = list(filter(lambda n: n%2==0, nums))

print(evens)

doubles = list(map(lambda n: n+n,evens))

print(doubles)

sum = reduce(lambda a,b: a+b, doubles)

print(sum)


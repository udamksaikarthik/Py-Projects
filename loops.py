# Loops

# While loop
# Nested loop
i = 1
j = 1
while i <= 5:
    print("Karthik", end=" ")

    while j<=5:
        print('Rocks!!', end=" ")
        j += 1
    i += 1
    j = 1
    print('\n')

data = ['Karthik', 'Gayathri', 'Rudhvedh','Python','Rakthapinjiri roii']
# For Loop
for value in data:
    print(value)

# break and continue
for value in range(10):
    if value == 0:
        continue
    if value == 9:
        break
    print(value)

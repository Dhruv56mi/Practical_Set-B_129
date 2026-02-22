# Inverted Right Half Pyramid Pattern
num = 1
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
        if num > 9:
            num = 1
    print()
# Practical A4 code 
num = 1

for i in range(5, 3, -1):   # 5 and 4
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Reset number
num = 1

# Next three rows
for i in range(3, 0, -1):   # 3, 2, 1
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
# Even Numbers from 1 to 100

even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers between 1 to 100:")
print(even_numbers)

print("Minimum even number:", min(even_numbers))
print("Maximum even number:", max(even_numbers))
print("Sum of even numbers:", sum(even_numbers))

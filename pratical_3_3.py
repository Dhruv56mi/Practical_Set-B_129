# Odd numbers between 1 to 50
odd_numbers = [x for x in range(1, 51) if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Minimum 3 odd numbers
min_three = sorted(odd_numbers)[:3]
print("Three minimum odd numbers:", min_three)

# Maximum 3 odd numbers
max_three = sorted(odd_numbers)[-3:]
print("Three maximum odd numbers:", max_three)

# Average of odd numbers
average = sum(odd_numbers) / len(odd_numbers)
print("Average of odd numbers:", average)

# Practical 4A Code

# Create list of even numbers between 1 and 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]

# Display even numbers
print("Even numbers between 1 and 50:")
print(even_numbers)

# Three minimum even numbers
print("\nThree minimum even numbers:")
print(even_numbers[:3])

# Three maximum even numbers
print("\nThree maximum even numbers:")
print(even_numbers[-3:])

# Average of even numbers
average = sum(even_numbers) / len(even_numbers)

print("\nAverage of even numbers:")
print(average)
# Create a list
numbers = [10, 5, 20, 15, 25]

print("Original List:", numbers)

# 1. len()
print("Length of list:", len(numbers))

# 2. max()
print("Maximum value:", max(numbers))

# 3. min()
print("Minimum value:", min(numbers))

# 4. sum()
print("Sum of elements:", sum(numbers))

# 5. append()
numbers.append(30)
print("After append(30):", numbers)

# 6. insert()
numbers.insert(1, 12)
print("After insert(1,12):", numbers)

# 7. remove()
numbers.remove(20)
print("After remove(20):", numbers)

# 8. sort()
numbers.sort()
print("After sort():", numbers)
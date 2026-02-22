# Create a List

fruit = ["apple","mango","banana","orange"]
print("list created",fruit)

# Access List Elements

print("first element ",fruit[0])
print("last element ",fruit[-1])

# Update List

fruit [1] = "grapes"
print("after update",fruit)

fruit.append("chiko")
print("after adding",fruit)

# Delete List Elements

fruit.remove("orange")
print("after removing",fruit)

del fruit [0]
print("after deleting first element",fruit)

del fruit 
print ("list deleted succesfully")
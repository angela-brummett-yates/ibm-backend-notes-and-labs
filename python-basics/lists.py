# Learning Python Lists

#1. Creating a list 
fruits = ["apple", "banana", "cherry"]
print("Orginal List:", fruits)

print()

#2. Accessing items
print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Third Fruit:", fruits[2])

print()

#3. Changing an item
fruits[1] = "blueberry"
print("After the change:", fruits)

print()

#4. Adding items
fruits.append("orange")
print("After append:", fruits)

print()

#5. Removing items 
fruits.remove("apple")
print("After removing:", fruits)

print()

popped = fruits.pop(0)
print("Popped item:", popped)
print("After pop:", fruits)

print()

#6 Looping through a list 
print("Looping through list: ")
for fruit in fruits:
    print("Fruit:", fruits)
print()

#7 Checking membership
if "cherry" in fruits:
    print("Cherry is in the list")
else:
    print("Cherry is not in the list")  
print() 

#8 Length of list 
print("List length:", len(fruits))
print()

# Learning Python Dictionaries 

#1. Creating a dictionary
person = {
    "name": "Angela",
    "major": "Computer Science",
    "age": "40"
}
print("Orginial Dictionary:", person)

print()

#2. Accessing values
print("Name:", person["name"])
print("Major:", person["major"])

print()

#3. Adding new key/value pairs
person["city"] = "Dayton"
print("After adding city:", person)

print()

#4. Changing values
person["age"] = 41 
print("After updating age:", person)

print()

#5. Removing items
person.pop("age")
print("After pop:", person)

print()

#6. Looping through dictionary
print("Looping through keys:")
for key in person:
    print(key)
print()

print("Looping through values:")
for value in person.values():
    print(value)
print()

print("Looping through key/value pairs:")
for key, value in person.items():
    print(key, ":", value)
print()

#7. Checking if key exists 
if "name" in person:
    print("Name exists in dicitonary")
print()

#8 Nested dictionary
user = {
    "username": "angela",
    "profile": {
        "major": "Computer Science",
        "city": "Dayton"
    
    
    }
}
print("Nested value:", user["profile"]["city"])

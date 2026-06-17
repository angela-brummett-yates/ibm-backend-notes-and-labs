# Learning python loops

# 1. For loop example 
print("For loop example:")
for i in range(5):
    print("i is: ", i)

    print() #blank line for spacing

# 2. While loop example
print("While loop example:")
count = 0 
while count < 5:
    print("count is", count)
    count += 1

print()

#3. Looping through a list
print("Looping through a list:")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print("Fruit:", fruit)

print()

#4 Looping Until the users types stop 
print("Type 'stop' to end the loop.")
user_input = ""
while user_input != "stop":
    user_input = input("Enter something: ")
    print("You typed: ", user_input)



word = "Hello World!"
my_list = ['Bob', 'Alice', 'Eve']
print(len(word))  # Output: 12
print(len(my_list))  # Output: 3

text = "Hello, Python!"


#String slicing examples
# Traverse first 5 characters
print(text[0:5]) # Hello

# Traverse from index 7 to end
print(text[7:]) # Python!

# Traverse entire string
print(text[:]) # Hello, Python!


#String Functions
print ("String Functions\n")
print(text.lower())  # hello, python!
print(text.upper())  # HELLO, PYTHON!
print(text.replace("Python", "World"))  # Hello, World!
print(text.split(","))  # ['Hello', ' Python!']
print(text.find("Python"))  # 7
print(text.find("Java"))  # -1 (not found)


print ("\nList Functions\n")
#Lists - basic Information (creating, traversing, changing values (mutability), append, reverse and String interactions)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple   
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
fruits.append("date")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']
fruits.reverse()
print(fruits)  # ['date', 'cherry', 'blueberry', 'apple']


print ("\nMore List Functions\n")
#Lists - all functions: append(item), reverse(), remove(item), sort(), count(item), insert(location, item), index(item)
numbers = [4, 2, 7, 1, 3]
numbers.sort()
print("Sort:",numbers)  # [1, 2, 3, 4, 7]
numbers.remove(2)
print("Remove 2:",numbers)  # [1, 3, 4, 7]
print(numbers.count(3))  # 1
numbers.insert(1, 5)
print("Insert 1,5:",numbers)  # [1, 5, 3, 4, 7]
print("Index 4:",numbers.index(4))  # 3
numbers.append(10)
print("Append 10",numbers)  # [1, 5, 3, 4, 7, 10]

#Files - Just reading from files. Opening a file and then the four different ways to read information from a file
print ("\nFile Reading\n")
try:    
    with open("romeo1.txt", "r") as file:
        print("Readline:")
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()
        
    with open("romeo1.txt", "r") as file:
        print("\nReadlines:")
        lines = file.readlines()
        for line in lines:
            print(line.strip())
        
    with open("romeo1.txt", "r") as file:
        print("\nIterating through file:")
        for line in file:
            print(line.strip())
        
    with open("romeo1.txt", "r") as file:
        print("\nRead entire file:")
        content = file.read()
        print(content.strip())
except FileNotFoundError:
    print("File 'romeo1.txt' not found.")
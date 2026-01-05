
def formatting():
    name = input ("Name:")
    sum = 10/3


    #print ("Hello, {}! my height is {:.2f} meters.".format(name, sum))
    print ("Hello, %s! my height is %.2f meters." % (name, sum))


def number_operations():
    a = 10
    b = 3

    print(a + b)  # Addition: 13
    print(a - b)  # Subtraction: 7
    print(a * b)  # Multiplication: 30
    print(a / b)  # Division (float): 3.3333...
    print(a // b) # Floor division (integer result): 3
    print(a % b)  # Modulus (remainder): 1
    print(a ** b) # Exponentiation: 10^3 = 1000

def math_module_demo():
    import math

    x = 16

    print(math.sqrt(x))     # Square root: 4.0
    print(math.pow(2, 3))  # Power: 8.0
    print(math.sin(math.pi/2))  # Trigonometry: 1.0
    print(math.cos(0))          # 1.0
    print(math.log(100, 10))    # Log base 10: 2.0
    print(math.exp(2))          # e^2 ≈ 7.389
    print(math.factorial(5))    # 120

def rounding_demo():
    import math
    num = 5.6789

    print(round(num))        # 6
    print(round(num, 2))     # 5.68
    print(round(num, 3))     # 5.679
    print(math.floor(num))   # 3 (round down)
    print(math.ceil(num))    # 4 (round up)

def random_demo():
    import random

    print(random.randint(1, 10))  # Random integer between 1 and 10
    print(random.random())         # Random float between 0.0 and 1.0
    choices = ['apple', 'banana', 'cherry']
    print(random.choice(choices))  # Random choice from list
    random.shuffle(choices)        # Shuffle list in place
    print(choices)

def for_loop_demo():
    fruits = ['apple', 'banana', 'cherry']
    print ("Fruits in the list:")    
    for fruit in fruits:
        print(fruit)

    print("Numbers from 0 to 4:")   
    for i in range(5):
        print(i)
def string_slicing_demo():
    text = "Hello, World!"
    print(text[0])        # 'H'
    print(text[7:12])    # 'World'
    print(text[:5])      # 'Hello'
    print(text[7:])      # 'World!'
    print(text[-1])      # '!'
    print(text[-6:-1])   # 'World'
def dict_demo():
    student_scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78
    }

    for name, score in student_scores.items():
        print(f"{name}: {score}")
#math_module_demo()
def enter_number():
    while True:
        try:  # Fault Tolerant Input, keep asking until valid input.  Graceful Error Handling.
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

def read_file_lines_demo():
    filename = "sample.txt"
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            print("File Lines:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def read_file_demo():
    filename = "grades.txt"
    try:
        with open(filename, "r") as f:
            content = f.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

#number_operations()
#rounding_demo()
#random_demo()
read_file_demo()
def remove_duplicates_ai(lst): 
    return list(set(lst))

#def: is a function or. named block of code that performs a specific task when called fro m elsewhere in the program.
# used to modularize code, making it reusable and easier to read.

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result: # check for duplicates.
            result.append(item)
    return result

def average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def mainmenu():
    options = ["Remove Duplicates", "Average of Numbers"]
    choice=0
    while choice !=9:
        print("Select an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = int(input("Enter choice (1-2, 9 to quit): "))
        if choice == 1:
            lst = input("Enter a list of items separated by commas: ").split(",")
            print("\nWithout duplicates:", remove_duplicates(lst))
        elif choice == 2:
            nums = list(map(float, input("Enter numbers separated by commas: ").split(",")))
            print("Average:", average(nums))
        elif choice == 9:
            print("Good bye.")
        else:
            print("Invalid choice. Please try again.")

def numbers():
    intNum = int(input("Enter integers separated by spaces: "))
    floatNum = float(input("Enter floats separated by spaces: "))

    print("Integers:", intNum) # whole numbers 1,2,3, 10,11, NOT 10.5
    print("Floats:", floatNum) # is  good for financle $10.50

def forRange():
    for i in range(5):  # 0,1,2,3,4
        print(i)
    print ("----")
    for i in range(2, 7):  # 2,3,4,5,6
        print(i)
    print ("----")

    for i in range(1, 10, 2):  # 1,3,5,7,9
        print(i)

def popExample():
    fruits = ["apple", "banana", "cherry", "date"]
    print("Original list:", fruits)

    popped_fruit = fruits.pop()  # removes and returns the last item
    print("Popped fruit:", popped_fruit)
    print("List after pop():", fruits)

    popped_fruit_index = fruits.pop(1)  # removes and returns item at index 1
    print("Popped fruit at index 1:", popped_fruit_index)
    print("List after pop(1):", fruits)
if __name__ == "__main__":
    popExample()

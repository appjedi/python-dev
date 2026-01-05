



def quiz_ex1():
    name="john smith"
    name_array=name.split(" ")

    print(name_array)
    print ("length of array:", len(name_array))

    for n in name_array: # traverse through each element of the array.
        print("loop:", n.title())
    #print(name.title()) # proper case.
    #print(name.capitalize()) # upper case.

    print("REPLACE EX:",name.replace("john", "jane")) # replace john with jane.

def quiz_ex2():
    s="the quick brown fox jumps over the lazy dog"
    letter =input("Enter a letter to count: ")
    num_of_the=s.count(letter)
    print("number of the:", num_of_the)


def int_quiz():
    num1=int(input("Enter first integer: "))
    num2=int(input("Enter second integer: "))
    print ("first integer:" + str(num1))
    print("sum:", num1+num2)
    print("difference:", num1-num2)
    print("product:", num1*num2)
    print("quotient:", num1/num2)
    print("integer quotient:", num1//num2)
    print("remainder:", num1%num2)
    print("power:", num1**num2) 

def int_float_quiz():
    num1=float(input("Enter first float: "))
    num2=int(input("Enter second float: "))


    print ("first float:" ,num1)
    print("first int:",num2)

def list_mutation_quiz():
    my_list=[10,20,30,40,50]
    print("original list:", my_list)
    my_list[2]=99 # change index 2 to 99
    print("after mutation:", my_list)
    my_list.append(60)
    print("after append:", my_list)
    my_list.insert(1,15)
    print("after insert:", my_list)
    my_list.remove(40)
    print("after remove:", my_list)
    popped_value=my_list.pop()
    print("after pop:", my_list)
    print("popped value:", popped_value)
    my_list.sort()
    print("after sort:", my_list)
    my_list.reverse()
    print("after reverse:", my_list)
    my_list.count(20)
    print("count of 20:", my_list.count(20))
    index_of_99=my_list.index(99)
    print("index of 99:", index_of_99)


def math_quiz():
    import random
    while True:
        num1=random.randint(1,100)
        num2=random.randint(1,100)
        print("What is", num1, "+", num2, "?")
        answer=int(input("Your answer: "))
        if answer==num1+num2:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", num1+num2)
        another=input("Do you want another question? (yes/no): ")
        if another.lower()!="yes":
            break

def main():
    #quiz_ex1()
    math_quiz()

main()
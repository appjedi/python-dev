

#num1=int(input("Enter an integer divisor: "))

def prompt_int(msg):
    while True:
        try: # Fault tolerant input, keeps asking until valid.  Graceful handling of ValueError.
            value = int(input(msg))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_file():
    filename = input("Enter the filename to read: ")

    with open(filename, "r") as file:
            for line in file:
                print(line.strip())


def read_file_try():
    while True:
        filename = input("Enter the filename to read: ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    print(line.strip())
            return
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")

read_file_try()


def try_except_example():
    try:
        result = 10 / int(num)
        print(f"Result is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Program ended.")
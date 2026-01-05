# Lab 22
# This lab

# Name
# Date

def insert_name(name,listy):
    # in this function, you will insert a given name
    # into the appropriate place in a list of names


    new_last = name.strip().split()[1]

    for i in range(len(listy)):
        current_last = listy[i].strip().split()[1]
        if new_last < current_last:
            listy.insert(i, name)
            return

    listy.append(name)





def main():
    # First, open the names.txt file,
    # and add the names of the people
    # into a list called all_names
    all_names = []
    files = open("names.txt", "r")
    all_names = files.readlines()
    files.close()

    # space for first task



    
    # Second, insert these names in the appropriate place alphabetically using the function 
    # insert_name you wrote above
    insert_name("Michaela Tracy\n", all_names)
    insert_name("Jeffrey Harris\n", all_names)
    insert_name("Sheera Knecht\n", all_names)
    # you should not need any additional code here for task 2

    

    # Last, write the all_names list to a new file called "newnames.txt".  
    # It should have the three names added correctly. 
    # space for third task
    new_file = open("newnames.txt", "w")
    for name in all_names:
        new_file.write(name)
    new_file.close()



main()
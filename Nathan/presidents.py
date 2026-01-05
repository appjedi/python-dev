def main():
    presidents = ["JohnQuincy Adams", "Joe Biden", "Richard Nixon", "Ronald Reagan", "Harry Truman"]

    new_name = input("Enter the new president: ")

    space_index = new_name.find(" ")
    new_first = new_name[:space_index]
    new_last = new_name[space_index + 1:]

    position = 0
    for i in range(len(presidents)):

        pres = presidents[i].find(" ")
        first = presidents[i][:pres]
        last = presidents[i][pres + 1:]
 

        if new_last < last or new_last == last and new_first < first:
            break
            
        position += 1
        


    presidents.insert(position, new_name)

    print(presidents)

    save_to_file(presidents, "presidents.txt")

def save_to_file(list, file_name):
    try:
        with open(file_name, "w") as f:
            for name in list: # traverse the list of students.
                f.write(name+"\n")
    except IOError:
        print ("file write error")

main()
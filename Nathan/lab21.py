script_list=[]
def read_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.split(" ")
                for word in words:
                    word = word.lower()
                    if word not in script_list:
                        script_list.append(word)
        script_list.sort()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def freq_count(search_str, word_list):
    """
    Prints each word along with the number of times
    search_str occurs as a substring within that word.
    Uses str.find() only.
    """
    for word in word_list:
        count = 0
        start = 0

        while True:
            pos = word.find(search_str, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1

        print(f"{word}: {count}")
        if count>20:
            return
        #print(count)

def main():
    read_file()
    another = 'y'
    while another == 'y':
        print("Unique words in the file:")
        #print(script_list)
        search_str = input("Enter a word to search for its frequency: ").strip().lower()
        freq_count(search_str, script_list)
        another = input("Do you want to search for another word? (y/n): ").strip().lower()

main()
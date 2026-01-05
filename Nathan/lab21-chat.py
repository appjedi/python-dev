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


def main():
    filename = input("Enter filename: ")

    script_list = []

    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()
                    if word not in script_list:
                        script_list.append(word)

        # Sort alphabetically
        script_list.sort()

        search_str = input("Enter search string: ").lower()

        freq_count(search_str, script_list)

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()

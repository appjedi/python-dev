 #Program 18
# This program asks a user three different times for a character string which will determine if any of the words in phrase are repeated, and display the repeated words in the order they occur in the phrase.

# Nathan Wang
# Date Completed: 11/24/2025 

def duplicate_words_bob(phrase):
    words = phrase.lower().split(" ")
    seen_words = []
    dupes = []
    for i in words:
        if i in seen_words and i not in dupes:
            dupes.append(i)
        else:
            seen_words.append(i)
    dupes.sort()
    newstr = ''
    for i in dupes:
        newstr += i
        newstr += ' '
    return newstr


def duplicate_words(phrase):
  words = phrase.split()
  dupes = []
  seen_words = []
  for word in words:
    if word in seen_words and word not in dupes:
      dupes.append(word)
    else:
      seen_words.add(word)
  return dupes

def remove_duplicates(list):
    new_list=[]
    for word in list:
        if word not in new_list:
            new_list.append(word)
    return new_list

def average(myList):
  if len(myList) == 0:
    return "ERROR"
  total = 0
  for number in myList:
    total += number
  return total/len(myList)

def testInput():
    phrase = ""
    for i in range(3):
        word=input("Welcome to the duplicate detector!")
        phrase += word + " "
    print("")
    print(f"Repeated words: {duplicate_words(phrase)}")
        # Split the input string into a list of words
def main():
    print("Welcome to Duplicate Detector!")
    for _ in range(3):
        phrase = input("Please enter a line for me to inspect: ")
        result = duplicate_words(phrase)
        if result:
            print(f"Duplicated words: {result}")
        else:
            print("No duplicated words found.")
def main1():
    testInput ()

def main():
  print("Welcome to the duplicate detector!")
  for i in range(3):
    phrase = input("Enter a phrase: ")

main()
  # This is where you write the duplicate word function
  # the variable phrase should be a string
  # the result is a printed list of repeating words displayed once each
  # in alphabetical order


  # This is where you will write the main components of your program, the looping, user input, and calling the duplicate_words function.

  # The program should loop three times receiving a line of input each time.

  # Delete the word pass and write your code there, then delete this comment
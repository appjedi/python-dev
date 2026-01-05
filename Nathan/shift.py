

def left_shift(word, X ):
    """Left shift the elements of the array by n positions."""
    if not word:
        return word
    X = X % len(word)  # Handle shifts greater than array length
    return word[X:] + word[:X]

def right_shift(word, n):
    """Right shift the elements of the array by n positions."""
    if not word:
        return word
    n = n % len(word)  # Handle shifts greater than array length
    return word[-n:] + word[:-n]


    
def main():
    print (right_shift("computers", 4))  # "lohel"
    print (left_shift("Aardvark", 2))  # "llohe"
    print (right_shift("ANTIDERIVATIVE", 9))  # "lohel"
    print (left_shift("RIEMANN", 2)) 
    print (left_shift("INTEGRATION", 5)) 
#  appjedi.net@gmail.com

main()
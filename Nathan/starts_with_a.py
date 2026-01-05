
def starts_with_a(s):
    words = s.lower().split(" ")
    result = [] # empty list to store results
    for word in words:
        if word.startswith('a'):
            if word not in result: # look for duplicates
                result.append(word)
    return " ".join(result)

def main():
    test1 = "Abby abby Beth Anna Adam Amy Zoe Zelda Amy Amy Derman anna"
    print(starts_with_a(test1))




    # -> ["a","b","c"]
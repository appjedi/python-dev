

def three_of_four(password):
    num=0
    if len(password)>=8:
        num += 1
    for c in password:
        if c >'a' and c <'z':
            num += 1
            break
    for c in password:
        if c >'A' and c <'Z':
            num += 1
            break
    for c in password:
        if c >'0' and c <'9':
            num += 1
            break
    for c in password:
        if c in "!@#$%&*":
            num += 1
            break

    return num >= 3 

def main():
    pw = input("Enter a password to test it's strength: ")
    print(three_of_four(pw))

if __name__ == "__main__":
    main()
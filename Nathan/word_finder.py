def finder(name_list, let):
    results = []
    let = let.upper()
    for name in name_list:
        #if name.upper().startswith(let):
        if name.upper()[:3] == let:
            results.append(name)

    return results

def finding(name_list,size):
    results = []
    for name in name_list:
        if len(name) == size:
            results.append(name)

    return results

def multiplier(list):
    results = []
    for i in list:
        results.append(i*3)
    return results

def main():
    name_list = ["Lets", "b", "c", "Letso"]
    let = input("Enter a letter(s): ")
    print(finder(name_list, let))

    #size=int(input("Enter a size: "))
    #print(finding(name_list, size))

    num_list = [1,2,3,4,5]
    #print(multiplier(num_list))

if __name__ == "__main__":
    main()
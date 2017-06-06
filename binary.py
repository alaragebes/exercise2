def binary_search (myItem, myList):
    found = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and not found :
        middle = ( bottom + top) // 2
        if myList [middle] == myItem :
            found = True
        elif myList [middle] < myItem :
            bottom = middle + 1
        elif myList [middle] > myItem :
            top = middle - 1
    return found

if __name__ == "__main__":
    numberList = [1, 2, 5, 8, 10, 14, 17, 18, 19, 24, 27, 28]
    print "Enter number: ",
    item = int(raw_input())
    isitfound = binary_search (item, numberList)
    if isitfound :
        print "Yes, in the list"
    else :
        print "No, number not in the list"

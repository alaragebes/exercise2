def linear_search (myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found :
        if myList[position] == myItem :
            found = True
        position = position + 1
        return found

if __name__ == "__main__":
    shopping = ["apples", "kiwi", "maple", "coconut"]
    print "What item?"
    item = raw_input(" ")
    isitfound = linear_search (item, shopping)
    if isitfound == True :
        print ("Your item is here")
    else :
        print ("Nope, not here.")

## couldn't find ERROR 


def bubble_sorted(myList):
    moreSwaps = True
    while moreSwaps :
        moreSwaps = False
        for position in range (len(myList) - 1) :
            if myList[position] > myList[position + 1]:
                moreSwaps = True
                temp = myList[position]
                myList[position] = myList[position + 1]
                myList[position + 1] = temp
    return myList

def test_bubble_sort():
    numberList = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
    sortedList = bubble_sorted(numberList)
    print (sortedList)

test_bubble_sort()

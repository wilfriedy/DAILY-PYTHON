numList = [1,13,4,54,-1]
if len(numList) > 0 :
    minNum = numList[0]
    maxNum = numList[0]
    counter = 1
    while len(numList)  > counter :
        tracker = numList[counter]
        if tracker > maxNum :
            maxNum = tracker
        if tracker < minNum:
            minNum = tracker
        counter += 1
    print(f"min : {minNum}")
    print(f"max : {maxNum}")
else:
    print("The list is empty")


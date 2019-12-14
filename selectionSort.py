def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        #print(i)是为了消除变量i unused的警告
        print (i)
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr = [5,3,6,2,10]
lastArr = []
lastArr = selectionSort(arr)
print (lastArr)
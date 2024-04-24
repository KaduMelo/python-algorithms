def searchMin(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        min = searchMin(arr)
        newArr.append(arr.pop(min))
    return newArr

print(selectionSort([1,6,8,10,11, 4, 2, 51, 40, 3]))
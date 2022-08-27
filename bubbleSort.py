def bubbleSort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                ## swap the elements in the array
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


## Driver code
arr =[70,29,50,30,90,5,15]
result = bubbleSort(arr)
print("Sorted array after applying bubble sort :", result)
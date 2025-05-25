def QuickSort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
   
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i],arr[j] = arr[j], arr[i]
            
        arr[i+1], arr[high] = arr[high], arr[i+1]
        QuickSort(arr, low, i)
        QuickSort(arr, i+2, high)

arr = [34, 11, 64, 5, 90, 12, 25, 22]
n = len(arr)
QuickSort(arr,0,n-1)
print("Sorted array:", arr)
        

            
        
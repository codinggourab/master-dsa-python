def InsertionSort(arr):
    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     j = i - 1
        
    #     while j >= 0 and key < arr[j]:
    #         arr[j+1] = arr[j]
    #         j -= 1
            
    #     arr[j+1] = key
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            
        
        
arr = [1, 11, 13, 5, 6]
InsertionSort(arr)
print("Sorted list:", arr)
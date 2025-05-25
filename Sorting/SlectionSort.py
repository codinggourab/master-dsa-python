def selectioSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
        
        
arr = [13,46,80,9,24]

selectioSort(arr)

print("Sorted array is: ",arr)

                
                
def Bubblesort(arr):
    n = len(arr)
    swap = False
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        swap = True
        
        if not swap:
            break
        
        
arr = [1,2,3,4,5,7]

Bubblesort(arr)

print("Sorted array is: ",arr)

        
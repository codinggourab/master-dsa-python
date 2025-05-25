def heapify(arr, n, i):
    larg = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        larg = l
    if r < n and arr[larg] < arr[r]:
        larg = r
        
        
        if larg != i:
            arr[i],arr[larg] = arr[larg], arr[i]
            heapify(arr, n, larg)
            
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    
    print("%d " % arr[i], end='')
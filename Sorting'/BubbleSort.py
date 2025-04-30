arr = [3,1,7,2,8,6,9]
n = len(arr)
swap = False
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swap = True
        if not swap:
            break
print("Sorted array is: ",arr)
        
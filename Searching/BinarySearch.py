def BInarySearch(a,low,high,key):
    mid = (low + high) // 2

    if low <= high:
        if a[mid] == key:
            print(f"{key} element is found at index",mid)
        elif a[mid] < key:
            BInarySearch(a,mid + 1,high,key)
        else:
            BInarySearch(a,low,mid - 1,key)
    if low > high:
        print("Element not found")


a = [20,30,10,80,90]
low = 0
high = len(a) - 1
key = 10
BInarySearch(a,low,high,key)
key = 1
BInarySearch(a,low,high,key)
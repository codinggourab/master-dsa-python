def LinearSearch(a,n,key):
    c = 0
    for i in range(n):
        if a[i] == key:
            print(f"{key} is present in the array")
            c += 1
       
    if c == 0:
        print(f"{key} is not present in the array")
        
        

a = [20,30,10,80,90]
n = len(a)
key = 10
LinearSearch(a,n,key)
key = 3
LinearSearch(a,n,key)
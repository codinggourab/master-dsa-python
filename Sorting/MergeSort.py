def mergesort(a, n):
   if n > 1:
      m = n // 2
      #divide the list in two sub lists
      l1 = a[:m]
      n1 = len(l1)
      l2 = a[m:]
      n2 = len(l2)
      #recursively calling the function for sub lists
      mergesort(l1, n1)
      mergesort(l2, n2)
      i = j = k = 0
      while i < n1 and j < n2:
         if l1[i] <= l2[j]:
            a[k] = l1[i]
            i = i + 1
         else:
            a[k] = l2[j]
            j = j + 1
         k = k + 1
      while i < n1:
         a[k] = l1[i]
         i = i + 1
         k = k + 1    
      while j < n2:
         a[k]=l2[j]
         j = j + 1
         k = k + 1
            
        

# Example usage
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergesort(arr, n)
print("Sorted array is:", arr)
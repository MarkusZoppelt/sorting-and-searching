arr = [35, 2, 45, 64, 99, 10]

# Runtime: O(n²) average and worst case. Memory: O(1)
def selectionSort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[index] > arr[j]:
               index = j
      
        arr[i], arr[index] = arr[index], arr[i]

selectionSort(arr)

print(arr)
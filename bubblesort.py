arr = [35, 2, 45, 64, 99, 10]

# O(n²)
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

bubblesort(arr)

print(arr)
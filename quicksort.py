arr = [35, 2, 45, 64, 99, 10]

# Runtime: O(m log(n)) average O(n^2) worst case. Memory: O(n log(n))
def quicksort(arr, left: int, right: int):
    index = partition(arr, left, right)
    if left < index - 1: # sort left half
        quicksort(arr, left, index - 1)
    if index < right: # sort right half
        quicksort(arr, index, right)

def partition(arr, left: int, right: int) -> int:
    pivot = arr[right] # pick pivot (here: last)
    while left < right:
        # find element on left that should be on right
        while arr[left] < pivot:
            left += 1

        # find element on right that should be on left
        while arr[right] > pivot:
            right -= 1
        
        # swap elements, nd move left and right indices
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left] # swaps elements
            left += 1
            right -= 1

    return left

quicksort(arr, 0, len(arr) - 1)

print(arr)
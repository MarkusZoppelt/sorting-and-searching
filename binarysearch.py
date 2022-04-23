arr = [2, 10, 32, 64, 77, 99]
find = 64

# O(log n)
def binarySearch(arr, find: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < find:
            low = mid + 1
        elif arr[mid] > find:
            high = mid - 1
        else:
            return mid
    
    return -1 # error

def binarySearchRecursive(arr, find: int, low: int, high: int) -> int:
    if low > high: return -1 # error
    
    mid = low + (high - low) // 2
    if arr[mid] < find:
        return binarySearchRecursive(arr, find, mid + 1, high)
    elif arr[mid] > find:
        return binarySearchRecursive(arr, find, low, mid - 1)
    else: 
        return mid

print(arr)

print("Binary search for " + str(find) + " resulted at index: " + str(binarySearch(arr, find)))
print("Binary search for " + str(find) + " resulted at index: " + str(binarySearchRecursive(arr, find, 0, len(arr) - 1)))
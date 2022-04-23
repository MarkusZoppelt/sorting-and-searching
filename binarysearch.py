arr = [2, 10, 32, 64, 77, 99]
find = 64

# O(log n)
def binary_search(arr, find: int) -> int:
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

def binary_search_recursive(arr, find: int, low: int, high: int) -> int:
    if low > high: return -1 # error
    
    mid = low + (high - low) // 2
    if arr[mid] < find:
        return binary_search_recursive(arr, find, mid + 1, high)
    elif arr[mid] > find:
        return binary_search_recursive(arr, find, low, mid - 1)
    else: 
        return mid

print(arr)

print("Binary search for " + str(find) + " resulted at index: " + str(binary_search(arr, find)))
print("Binary search for " + str(find) + " resulted at index: " + str(binary_search_recursive(arr, find, 0, len(arr) - 1)))
arr = [35, 2, 45, 64, 99, 10]

# Runtime: O(n log (n)) average and worst case. Memory: O(n)
def mergesort(arr, helper, low: int, high: int):
    if low < high:
        middle = low + (high - low) // 2
        mergesort(arr, helper, low, middle) # sort left half
        mergesort(arr, helper, middle + 1, high) # sort right half
        merge(arr, helper, low, middle, high) # merge them

def merge(arr, helper, low: int, middle: int, high: int):
    # copy both halfs into helper arr
    for i in range(low, high + 1):
        helper[i] = arr[i]
    
    helper_left = low
    helper_right = middle + 1
    curr = low

    # iterate through helper arr. Compare left and right half,
    # copying back the smaller element from the two halfes
    # into the original arr.
    while (helper_left <= middle and helper_right <= high):
        if helper[helper_left] <= helper[helper_right]:
            arr[curr] = helper[helper_left]
            helper_left += 1
        else: # if right element is smaller than left element
            arr[curr] = helper[helper_right]
            helper_right += 1
        curr += 1
    
    # copy the rest of the left side of the arr into target arr
    remaining = middle - helper_left
    for i in range(0, remaining + 1):
        arr[curr + i] = helper[helper_left + i]

# initialize a helper arr with length = len(arr)
helper = []
for i in range(0, len(arr)):
    helper.append(0)

mergesort(arr, helper, 0, len(arr) - 1)

print(arr)
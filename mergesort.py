arr = [35, 2, 45, 64, 99, 10]

# Runtime: O(n log (n)) average and worst case. Memory: O(n)
def mergeSort(arr, helper, low: int, high: int):
    if low < high:
        middle = low + (high - low) // 2
        mergeSort(arr, helper, low, middle) # sort left half
        mergeSort(arr, helper, middle + 1, high) # sort right half
        merge(arr, helper, low, middle, high) # merge them

def merge(arr, helper, low: int, middle: int, high: int):
    # copy both halfs into helper arr
    for i in range(low, high + 1):
        helper[i] = arr[i]
    
    helperLeft = low
    helperRight = middle + 1
    curr = low

    # iterate through helper arr. Compare left and right half,
    # copying back the smaller element from the two halfes
    # into the original arr.
    while (helperLeft <= middle and helperRight <= high):
        if helper[helperLeft] <= helper[helperRight]:
            arr[curr] = helper[helperLeft]
            helperLeft += 1
        else: # if right element is smaller than left element
            arr[curr] = helper[helperRight]
            helperRight += 1
        curr += 1
    
    # copy the rest of the left side of the arr into target arr
    remaining = middle - helperLeft
    for i in range(0, remaining + 1):
        arr[curr + i] = helper[helperLeft + i]

# initialize a helper arr with length = len(arr)
helper = []
for i in range(0, len(arr)):
    helper.append(0)

mergeSort(arr, helper, 0, len(arr) - 1)

print(arr)
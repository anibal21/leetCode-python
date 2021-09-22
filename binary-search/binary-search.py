def binarySearch(arr, target):
    left = 0 # O(1)
    right = len(arr) -1 # O(1)

    while(left <= right): # O(log N)
        mid = (left + right) // 2 # whole number division # O(1)

        if (arr[mid] == target): # O(1)
            return mid # O(1)
        elif (arr[mid] < target): # O(1)
            left = mid + 1 # O(1)
        else: 
            right = mid - 1 # O(1)
    
    return -1 # O(1)

arr = [1,2,3,4,5,6] # O(1)
target = 6 # O(1)

result = binarySearch(arr, target) # O(log N) * O(5) = O(log N)

if result != -1: # O(1)
    print("Element is present at index %d" % result) # O(1)
else:
    print("Element is not present in the array") # O(1)

# The algorithm has O(log N) complexity
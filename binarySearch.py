# Performs a binary search on an array for a target x
# Returns index of search target (-1 if not in array)
def binarySearch(array, left, right, x):

    # While there's still array elements left to check
    while left <= right:

        # Calculate mid point
        mid = (left + right-1) // 2

        # If the midpoint value matches the target
        if array[mid] == x:
            return mid
        
        # If the midpoint value is less than target, ignore left side of array
        elif array[mid] < x:
            left = mid + 1

        # If the midpoint value is greater than target, ignore right side of array
        else:
            right = mid - 1

    # Return -1 if target is not present in array
    return -1


def main():
    # Array to test on
    array = [2, 4, 13, 19, 23, 34, 37, 51, 59, 62, 63]

    # Target number to search for
    x = 51

    target_index = binarySearch(array, 0, len(array)-1, x)

    if target_index == -1:
        print("Element " + str(x) + " not found in array.")
    else:
        print("Target element " + str(x) + " found at index " + str(target_index) + ".")

main()

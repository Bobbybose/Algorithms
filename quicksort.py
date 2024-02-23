# Performs quicksort on an array 
def quicksort(array, low, high):
    if low < high:

        # Number to pivot on
        # Choosing rightmost index
        pivot = array[high]

        # Index of partition 
        # Eventually pivot index
        partition = low

        # Traversing the array and comparing each number to pivot
        for i in range(low, high):

            # If the number is less than the pivot
            if array[i] <= pivot:
                # Swapping current number with partition index number
                # Moving the low number below pivot
                array[i], array[partition] = array[partition], array[i]

                # Incrementing partition index
                partition += 1

        # Swapping pivot with next greatest number (partition index)
        # Pivot is now at partition index
        array[high], array[partition] = array[partition], array[high]

        # Uncomment to see array after each traversal
        # print(array)

        # Recursively quicksort the left hand of partition
        quicksort(array, low, partition - 1)

        # Recursively quicksort the right hand of partition
        quicksort(array, partition + 1, high)


# Main function
def main():
    # Array to sort
    array = [12, 4, 81, 45, 32, 82, 90, 51, 73]
    
    # Printing original array
    print("Original array: " + str(array))

    # Performing quicksort on the array
    quicksort(array, 0, len(array)- 1)
    
    # Printing sorted array
    print("Sorted array:   " + str(array))


main()
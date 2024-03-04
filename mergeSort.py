# Performs mergeSort on an array
def mergeSort(array):
    # As long as the array is at least 2 elements long
    if len(array) > 1:

        # Midpoint index of array
        mid_index = len(array)//2

        # Copying left and right of array into their own subarrays
        left = array[:mid_index]
        right = array[mid_index:]

        # Performing mergeSort recursively on the left and right subarrays
        mergeSort(left)
        mergeSort(right)

        # Current index of element being compared in the arrays
        left_index = right_index = array_index = 0
        
        # Until either subarray has no more elements remaining
        while left_index < len(left) and right_index < len(right):
            
            # If the left element if smaller or equal to the right element
            if left[left_index] <= right[right_index]:
                # Add it to the main array
                array[array_index] = left[left_index]
                # Move to next element in left subarray
                left_index += 1
            # Otherwise if the right element is smaller               
            else:
                # Add it to the main array
                array[array_index] = right[right_index]
                # Move to next element in right subarray
                right_index += 1
            
            # Move to next index in the main array
            array_index += 1
        
        # If there are any elements remaining in the left subarray add them to the main array
        while left_index < len(left):
            array[array_index] = left[left_index]
            left_index += 1
            array_index += 1

        # If there are any elements remaining in the right subarray add them to the main array
        while right_index < len(right):
            array[array_index] = right[right_index]
            right_index += 1
            array_index += 1

# Main function
def main():
    # Array to sort
    array = [12, 4, 81, 45, 32, 82, 90, 51, 17, 73, 103, 61]
    
    # Printing original array
    print("Original array: " + str(array))

    # Performing mergeSort on the array
    mergeSort(array)
    
    # Printing sorted array
    print("Sorted array:   " + str(array))


main()
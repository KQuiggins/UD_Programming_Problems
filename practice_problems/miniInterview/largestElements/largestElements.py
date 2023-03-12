def largest_elements(arr, k):
    # Sort the input array in ascending order
    arr.sort()

    # Initialize a list to store the k largest elements
    largest = []

    # Iterate over the sorted array in reverse order
    for i in reversed(arr):
        # If we've found k elements, return the list
        if len(largest) == k:
            return largest

        # Otherwise, append the current element to the list of largest elements
        largest.append(i)

    # If there are fewer than k elements in the input array, return the entire array
    return largest

# Test the solution
arr = [5, 16, 7, 9, -1, 4, 3, 11, 2]
k = 4
answer = largest_elements(arr, k)
print(answer)

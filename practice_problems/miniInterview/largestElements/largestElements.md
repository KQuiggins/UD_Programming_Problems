# Mini Interview Question: Largest Elements

## Goal: Solve this problem in < 30 minutes

## Question

Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns the `k` largest values from that array. The order of the elements in the returned array doesn’t matter.

## Example

- Input array: `[5, 16, 7, 9, -1, 4, 3, 11, 2]`
- `k`: 3
- Result: `[16, 9, 11]`

## My Approach

To find the k largest elements in the array, we need to sort the array in ascending order and then iterate over the sorted array in reverse order, adding each element to a list of largest elements until the list contains k elements.

If the input array contains fewer than k elements, we return the entire array.

## Solution

In my implementation, I first sort the input array in ascending order using the sort() method. I then initialize an empty list largest to store the `k` largest elements.

I then iterate over the sorted array in reverse order using the reversed() function. For each element in the sorted array, I check if I have already found k elements. If I have, I return the list of largest elements.

If I haven't found k elements yet, I append the current element to the list of largest elements.

Finally, if there are fewer than k elements in the input array, I return the entire array.

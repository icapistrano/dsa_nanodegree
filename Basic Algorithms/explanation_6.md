# Problem 6: Max and Min in a Unsorted Array

To find the max and min in an unsorted array:

1. Initialise pointers: low to track the minimum value visited and high to track the maximum value visited. The low and high are initialised to the first item in array.
2. Traverse array linearly and update low if the item is smaller than the current low value, and update high if the item is higher than the current high value.

So, time complexity is O(n) for traversing the array and O(1) for only keeping track of low and high pointers.

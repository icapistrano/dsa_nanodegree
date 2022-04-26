# Problem 2: Search in a Rotated Sorted Array

Binary Search was used to find the item in a rotated sorted array.

To find the index of the target value if it exist in the array.

1. Initialise a left and right pointer with left=0 and right=len(arr)-1.
2. Locate the middle element and return the middle index if it matches the target value.
3. If not, check if we are either on the left/right portion.
4. If we are on the left portion: search the right side if the middle element is less than the target or if target is less than the value at index left. Else, search the left side.
5. If we are on the right portion: search the left side if the middle element is greater than the target or if the target is greater than the value at index right. Else, search right side.
6. Return -1 if the while loop finishes.

So, time complexity is O(logn) for binary search and space complexity O(1).

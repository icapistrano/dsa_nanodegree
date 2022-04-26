# Problem 4: Dutch National Flag Problem

I maintained 3 pointers for tracking indexes of low (0), mid (1) and high (2).

I traversed through the array with 3 conditions:

1. If item is 0, swap the items at indexes low and high, then increment low and mid by 1.
2. If item is 1, increment mid by 1.
3. If item is 2, swap the items at indexes mid and high, then decrement high by 1.

So, time complexity is O(n) for traversing the array and space complexity is O(1) as we are swapping the items in-place.

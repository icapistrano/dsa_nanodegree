# Problem 1: Finding the Square Root of an Integer

I used binary search to find the square root of an input number. The return value should be less than or equal to the input number, therefore, I set the initial pointer to:

- left pointer: starts at 0
- right pointer: input number

There is no need for auxiliary data structure as we are simply using binary search.

So, time complexity is O(logn) and space complexity is O(1).

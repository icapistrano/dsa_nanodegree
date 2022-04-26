# Problem 3: Rearrange Array Elements

Firstly, I used merge sort to sort the array in descending order.

I constructed the two numbers with maximum sum by:

1. Traversing through the sorted array with an initial i=0 and j=1.
2. Appending i to the first list and j to the second list.
3. Incrementing i and j by 2.
4. Combining the digits together in each list, after the array traversal.

The sum of the result 2 numbers should be the largest possible value.

So, time complexity is O(nlogn) for sorting the array and space complexity is O(n) for constructing the 2 values in an array.

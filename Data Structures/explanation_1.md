# Problem 1: LRU Cache

I used a hash table to store keys and its corresponding node for a fast lookup of constant time.

I used a doubly linked-list to keep track of the least recently used node for removal and the most recently used node for insertion. Both operations are constant time.

As a tradeoff, nodes are stored in the hash table and in the linked-list with a linear space complexity.

So, time complexity is O(1) and space complexity is O(n).

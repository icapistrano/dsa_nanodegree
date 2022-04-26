# Problem 3: Data Compression

### Time/Space complexity of methods
**build_letter_lookup**: Iterate through each character and store character and frequency in a hash table. Time and space complexity is O(n).

**heapify**: create node with character and frequency data in hash table. Time and space complexity is O(n).

**merge_tress**: Remove two nodes with the minimum frequency, create node with sum of two nodes' frequency and reinsert into tree. Time complexity for removing is O(1) and reinserting is O(log n).

**assign_bits**: Assign bits from root to all leaf nodes. Time complexity is O(n).

**huffman_encoding**: calls all functions above and return encoding bits in string and a pointer to the root node.

**huffman_decoding**: Iterate through each bit and traverse tree until leaf node is reached. Repeats until all bits are iterated. Time complexity is O(n). 

So, for huffman encoding time complexity is O(n log n) and space complexity is O(n). For huffman decoding, time complexity is O(n).
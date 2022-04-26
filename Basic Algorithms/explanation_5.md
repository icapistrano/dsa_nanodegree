# Problem 5: Autocomplete with Tries

A Trie and TrieNode classes were implemented.

The **Trie** class has a root TrieNode, and insert and find methods.

##### Trie Efficiency

- insert: time complexity is O(n) where n is the length of the prefix, space complexity is O(1).
- find: time complexity is O(n) where n is the length of the prefix and space complexity is O(1).

The **TrieNode** class contains a word_complete attribute to indicate whether the word is complete and a hash table with character as key and a pointer to a TrieNode class as value. It has insert and suffixes methods:

##### TrieNode Efficiency

- insert: time complexity is O(1), space complexity is O(1).
- suffixes: time complexity is O(M * N) where M is the number of children per node and N is the depth Trie Tree.  Space complexity is O(M * N) where M is the length of a word (number of letters), and N the number of words in the tree.

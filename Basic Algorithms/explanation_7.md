# Problem 5: HTTPRouter using a Trie

A Router, RouteTrie and RouteTrieNode classes were implemented.

The **Router** class has a route trie RouteTrie, and add_handler, lookup and split_path methods.

##### Router Efficiency

- split_path: time complexity is O(n) for splitting the string path with built-in split. Space complexity is O(n) where n is the length of the array from splitting the url with delimeter '/'.
- add_handler: same efficiency as split path.
- lookup: same efficiency as split path.

The **RouteTrie** class has a root RouteTrieNode, and insert and find methods.

##### RouteTrie Efficiency

- insert: time complexity is O(n) and space complexity is O(1).
- find: time complexity is O(N * M) where N is the length of the length of the route and M is the depth of the route. Space complexity is O(1).

The **RouteTrieNode** class has a handler either None or a string, and a children with url path as key and a pointer to a RouteTrieNode as value. It has an insert method.

##### RouteTrieNode Efficiency

- insert: time complexity is O(1), space complexity is O(n) where n is the length of the route.

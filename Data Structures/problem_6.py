class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist1, llist2):
    visited = []
    llist = LinkedList()
    
    node = llist1.head
    while node:
        if node.value not in visited:
            llist.append(node.value)
            visited.append(node.value)
        
        node = node.next

    node = llist2.head
    while node:
        if node.value not in visited:
            llist.append(node.value)
            visited.append(node.value)
        
        node = node.next

    return llist


def intersection(llist1, llist2):
    llist1_visited = set()
    llist = LinkedList()
    
    node = llist1.head
    while node:
        if node.value not in llist1_visited:
            llist1_visited.add(node.value)
        
        node = node.next

    node = llist2.head
    while node:
        if node.value in llist1_visited:
            llist1_visited.remove(node.value)
            llist.append(node.value)
        
        node = node.next

    return llist


# helper function to create linked list from arr
def create_llist(arr):
    llist = LinkedList()

    for node in arr:
        llist.append(node)
    return llist

# helper function to turn linked list into set
def llist_to_set(llist):
    node_values = set()
    node = llist.head

    while node:
        if node.value in node_values:
            return False

        node_values.add(node.value)
        node = node.next

    return node_values

# check custom union and intersection functions to built in functions
def testcase(arr1, arr2):
    llist1 = create_llist(arr1)
    llist2 = create_llist(arr2)

    union_list_as_set = llist_to_set(union(llist1, llist2))
    if union_list_as_set == set(arr1).union(set(arr2)):
        print("Test union passed")
    else:
        print("Test union failed")

    intersection_llist_as_set = llist_to_set(intersection(llist1, llist2))
    if intersection_llist_as_set == set(arr1).intersection(set(arr2)):
        print("Test intersection passed")
    else:
        print("Test intersection failed")

    return union_list_as_set, intersection_llist_as_set


union_llist, intersection_llist = testcase([1,2,3,4,5,6], [5,6,7,8,9,10])
# expected output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6}

union_llist, intersection_llist = testcase([3,2,4,35,6,65,6,4,3,21], [6,32,4,9,6,1,11,21,1])
# expected output: {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21} {4, 21, 6}

union_llist, intersection_llist = testcase([0], [0,0,0])
# expected output: {0} {0}

union_llist, intersection_llist = testcase([], [0,0,0])
# expected output: {0} {}

union_llist, intersection_llist = testcase([], [])
# expected output: {} {}
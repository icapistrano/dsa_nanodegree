class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):
    def __init__(self, capacity=0):
        self.capacity = capacity if isinstance(capacity, int) else -1 # handle non integers
        self.cache = dict()
        self.head = Node("l-head", None)
        self.tail = Node("l-tail", None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)

        if node is None:
            return -1
    
        self.update_node_neighbours(node)
        self.add_at_start(node)
        return node.value

    def set(self, key, value):
        new_node = None
        if key in self.cache:
            new_node = self.cache[key]
            new_node.value = value
            self.update_node_neighbours(new_node)
        else:
            new_node = Node(key, value)

        self.cache[key] = new_node
        self.add_at_start(new_node)

        if len(self.cache) > self.capacity:
            delete_node_key = self.remove_at_end()
            del self.cache[delete_node_key]

    def update_node_neighbours(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_at_start(self, node):
        f_node = self.head.next
        f_node.prev = node
        node.next = f_node
        node.prev = self.head
        self.head.next = node

    def remove_at_end(self):
        l_node = self.tail.prev
        l_node.prev.next = self.tail
        self.tail.prev = l_node.prev
        return l_node.key

    def get_cache(self):
        cache = []
        node = self.head
        while node:
            if node != self.head and node != self.tail:
                cache.append(node.value)

            node = node.next

        return cache



def testcase1(expected_output):
    get_checks = []

    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    get_checks.append(our_cache.get(1) == 1)
    get_checks.append(our_cache.get(2) == 2)
    get_checks.append(our_cache.get(9) == -1)

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    get_checks.append(our_cache.get(3) == -1)


    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()


def testcase2(expected_output):
    get_checks = []

    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)

    get_checks.append(our_cache.get(1) == 1)

    our_cache.set(1, "text value")
    get_checks.append(our_cache.get(1) == "text value")

    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()


def testcase3(expected_output):
    get_checks = []

    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, None)

    get_checks.append(our_cache.get(2) == 2)
    get_checks.append(our_cache.get(1) == 1)
    get_checks.append(our_cache.get(3) == None)

    get_checks.append(our_cache.get(None) == -1)

    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()


def testcase4(expected_output):
    get_checks = []

    our_cache = LRU_Cache()

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)

    get_checks.append(our_cache.get(2) == -1)
    get_checks.append(our_cache.get(1) == -1)
    get_checks.append(our_cache.get(3) == -1)

    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()


def testcase5(expected_output):
    get_checks = []

    our_cache = LRU_Cache(-1)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)

    get_checks.append(our_cache.get(2) == -1)
    get_checks.append(our_cache.get(1) == -1)
    get_checks.append(our_cache.get(3) == -1)

    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()


def testcase6(expected_output):
    get_checks = []

    our_cache = LRU_Cache(None)

    our_cache.set(1, 1)
    our_cache.set(2, 2)

    get_checks.append(our_cache.get(1) == -1)
    get_checks.append(our_cache.get(2) == -1)

    if our_cache.get_cache() == expected_output and False not in get_checks:
        print("Test passed")
    else:
        print("Test failed")

    return our_cache.get_cache()



testcase1_cache = testcase1([6, 5, 2, 1, 4])
# expected output: [6, 5, 2, 1, 4]

testcase2_cache = testcase2(["text value", 3, 2])
# expected output: ["text_value", 3, 2]

testcase3_cache = testcase3([None, 1, 2])
# expected output: [None, 1, 2]

testcase4_cache = testcase4([])
# expected output: []

testcase5_cache = testcase5([])
# expected output: []

testcase6_cache = testcase6([])
# expected output: []
class Node:
    def __init__(self, character=None, frequency=None) -> None:
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

class MinHeap:
    def __init__(self) -> None:
        self.nodes = []
        self.size = 0

    def get_left_child_index(self, i):
        return (i * 2) + 1

    def get_right_child_index(self, i):
        return (i * 2) + 2

    def get_parent_index(self, i):
        return (i - 1) // 2

    def has_left_child(self, i):
        return self.get_left_child_index(i) < self.size
    
    def has_right_child(self, i):
        return self.get_right_child_index(i) < self.size

    def has_parent(self, i):
        return self.get_parent_index(i) >= 0

    def get_left_child(self, i):
        return self.nodes[self.get_left_child_index(i)]
    
    def get_right_child(self, i):
        return self.nodes[self.get_right_child_index(i)]

    def get_parent(self, i):
        return self.nodes[self.get_parent_index(i)]

    def peek(self):
        if self.size == 0:
            return
        return self.nodes[0]

    def swap(self, index1, index2):
        self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]

    def add(self, node):
        self.nodes.append(node)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index).frequency > self.nodes[index].frequency:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def poll(self):
        if self.size == 0:
            return None

        self.swap(0, self.size - 1)
        min_node = self.nodes.pop()
        self.size -= 1
        self.heapify_down()
        return min_node

    def heapify_down(self):
        index = 0
        
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.get_right_child(index).frequency < self.get_left_child(index).frequency:
                smaller_child_index = self.get_right_child_index(index)

            if self.nodes[index].frequency < self.nodes[smaller_child_index].frequency:
                return
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index

    def heapify(self, ch_freq):
        for ch, freq in ch_freq.items():
            node = Node(ch, freq)
            self.add(node)

    def __repr__(self) -> str:
        return " | ".join(str(node.frequency) for node in self.nodes)

# build table for character: frequency of character
def build_letter_lookup(string):
    letters = {}
    for ch in string:
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
    return letters


# merge nodes/tress and sort in priority queue
def merge_trees(tree):
    while tree.size != 1:
        n1, n2 = tree.poll(), tree.poll()
        node = Node(frequency = n1.frequency + n2.frequency) 
        node.left_child, node.right_child = n1, n2
        tree.add(node)

    return tree.poll()

# assign bits to leaf nodes built from root node. left=0, right=1
def assign_bits(tree):
    node_lookup = {}
    bits = []
    def traverse(node):
        # leaf node found
        if node.left_child is None and node.right_child is None:
            node_lookup[node.character] = "".join(bits.copy())
            return

        if node.left_child is not None:
            bits.append(str(0))
            traverse(node.left_child)
            bits.pop()

        if node.right_child is not None:
            bits.append(str(1))
            traverse(node.right_child)
            bits.pop()
        
    traverse(tree)
    return node_lookup

# encode each letter with its corresponding leaf node bits
def encode_str(string, ch_character):
    return "".join([ch_character[ch] for ch in string])



def huffman_encoding(data):
    tree = MinHeap()

    ch_frequency = build_letter_lookup(data) # build character: frequency table
    tree.heapify(ch_frequency) # build node and sort in priority queue

    # handle single character
    if tree.size == 1:
        tree_root = tree.peek()
        left_node = Node(tree_root.character, tree_root.frequency)
        tree_root.left_child = left_node
    else:  
        tree_root = merge_trees(tree)

    node_lookup = assign_bits(tree_root) # assign bit to leaf nodes starting from root
    encoded_string = encode_str(data, node_lookup) # encode original string with leaf node bits
    return encoded_string, tree_root


def huffman_decoding(encoded_str, tree):
    ch_index = 0
    decoded_string = []

    def decode(node, index):
        if node.left_child is None and node.right_child is None:
            return index, node.character

        if encoded_str[index] == '0':
            return decode(node.left_child, index+1)

        if encoded_str[index] == '1':
            return decode(node.right_child, index+1)

    while ch_index <= len(encoded_str) - 1:
        ch_index, leaf_ch = decode(tree, ch_index)
        decoded_string.append(leaf_ch)
    
    return "".join(decoded_string)


def testcase(expected_output):
    try:
        encoded_str, tree = huffman_encoding(expected_output)

        if huffman_decoding(encoded_str, tree) == expected_output:
            print("Test passed")
        else:
            print("Test failed")
            print(huffman_decoding(encoded_str, tree))

        return encoded_str

    except AttributeError as e:
        print("Input cannot be empty")

    except TypeError:
        print("Input cannot be an int, expected str")

if __name__ == "__main__":
    testcase("AAAAAAABBBCCCCCCCDDEEEEEE")
    # expected output: 1010101010101000100100111111111111111000000010101010101

    testcase("123")
    # encoded output: 10110

    testcase("1 L3ARN3D PR10R1TY QU3U3S!")
    # expected output: 10000111100101111010111100010111010001111100111001111101
    
    testcase(1)
    # Exception Error

    testcase("AAAAAA")
    # expected output: 000000

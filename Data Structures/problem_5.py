import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        encoded_data = hashlib.sha256(self.data.encode("utf-8"))
        encoded_timestamp = hashlib.sha256(self.timestamp.encode("utf-8"))
        encoded_timestamp.hexdigest()
        encoded_data.update(encoded_timestamp.digest())

        if self.previous_hash is not None:
            encoded_data.update(self.previous_hash.hash.encode("utf-8"))

        return encoded_data.hexdigest()


class Blockchain:
    def __init__(self):
        self.tail = None
        self.head = None

    def get_timestamp(self):
        return str(datetime.utcnow())

    def append_block(self, data=""):
        timestamp = self.get_timestamp()

        if self.tail is None:
            self.tail = Block(timestamp, data, None)
            self.head = self.tail
            return

        tail = self.tail
        block = Block(timestamp, data, tail)
        self.tail = block

    def traverse_nodes(self):
        nodes = []
        node = self.tail
        while node:
            nodes.append(node.data + " -> ")
            node = node.previous_hash
        return "".join(nodes)


def testcase1(nodes, expected_output):
    # Block Created
    blockchain = Blockchain()
    for node in nodes:
        blockchain.append_block(node)

    if blockchain.traverse_nodes() == expected_output:
        print("Test passed")
    else:
        print("Test failed")


def testcase2(nodes, expected_output):
    # Block Created
    blockchain = Blockchain()
    for node in nodes:
        blockchain.append_block(node)

    blockchain2 = Blockchain()

    if blockchain2.traverse_nodes() == expected_output:
        print("Test passed")
    else:
        print("Test failed")


def testcase3():
    blockchain = Blockchain()

    blockchain.append_block("one")
    t1 = blockchain.head.timestamp

    blockchain.append_block("two")
    t2 = blockchain.head.timestamp

    blockchain.append_block("three")
    t3 = blockchain.head.timestamp

    if t1 == t2 == t3:
        print("Test passed")
    else:
        print("Test failed")





if __name__ == "__main__":
    
    testcase1_input = ["This", "is", "my", "blockchain"]
    testcase1(testcase1_input, "".join([i + " -> " for i in reversed(testcase1_input)]))
    # expected output is blockchain -> my -> is -> This ->, where node points to its previous hash

    testcase1_input = ["original", "updated"]
    testcase1(testcase1_input, "".join([i + " -> " for i in reversed(testcase1_input)]))

    testcase1_input = ["block1", "block2", "block3", "block4", "block5"]
    testcase1(testcase1_input, "".join([str(i) + " -> " for i in reversed(testcase1_input)]))

    testcase2_input = ["block", "chain", "1"]
    testcase2(testcase2_input, "")
    # <empty str> no  nodes in blockchain 2

    testcase3()
    # all timestamp for head ref should be the same
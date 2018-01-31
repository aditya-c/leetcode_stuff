# This is double linked list implementation of LRU cache


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.key) + ":::" + str(self.value)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.contents = {}  # contains nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.contents:
            query_node = self.contents[key]
            self.remove(query_node)
            self.add(query_node)
            return query_node.value
        return -1

    def put(self, key, value):
        # remove the if it was already there
        if key in self.contents:
            self.remove(self.contents[key])

        # create and put the node
        new_node = Node(key, value)
        self.add(new_node)
        self.contents[key] = new_node

        # if Overflow: remove from top of list
        if len(self.contents) > self.capacity:
            victim_node = self.head.next
            self.remove(victim_node)
            del self.contents[victim_node.key]

        return self.contents.items()

    def add(self, new_node):
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def remove(self, victim_node):
        prev = victim_node.prev
        after = victim_node.next
        prev.next = after
        after.prev = prev


cache = LRUCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))       # returns 1
print(cache.put(3, 3))    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.put(4, 4))    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4

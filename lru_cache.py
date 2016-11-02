''' Minimal implementation of an LRU cache which implements addition, deletion and retrieval in O(1)'''
class Node(object):
    def __init__(self, key, value):
        ''' A node in a doubly linked list '''
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

        
class LRU(object):
    
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.cache = {}
        self.start_node = None
        self.end_node = None
        
    def add(self, key, value):
        ''' Add a value to the cache '''
        if key in self.cache: # If key is in the cache, refresh 
            self.remove(key)

        node = Node(key, value)

        if not len(self.cache): # Cache is empty
            self.start_node = node
            self.end_node = node
            self.cache[key] = node

        else:
            if len(self.cache) >= self.capacity: # If things are overflowing - remove the oldest node
                self.remove(self.start_node.key)

            # Setting up pointers to appropriate pieces
            node.prev = self.end_node
            self.end_node.next = node
            # Inserting node and marking it as the newest addition
            self.cache[key] = node
            self.end_node = node                                    

        return    
    
    def retrieve(self, key): 
        ''' Get a value given a key '''
        if key in self.cache:
            value = self.cache[key].value
            self.remove(key)
            self.add(key, value)
            return value

    def remove(self, key): 
        ''' Delete a key from the LRU cache '''
        next_node = self.cache[key].next
        prev_node = self.cache[key].prev

        if self.cache[key] == self.start_node:
            self.start_node = next_node

        if self.cache[key] == self.end_node:
            self.end_node = prev_node

        if prev_node: prev_node.next = next_node
        if next_node: next_node.prev = prev_node
        del self.cache[key]
        

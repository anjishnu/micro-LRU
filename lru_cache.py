
class Node(object):
    def __init__(self, key, value):
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
        if key in self.cache: # If key is in the cache, we refresh it. 
            self.remove(key)

        node = Node(key, value)

        if len(self.cache) == 0: # Cache is empty
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
        if key in self.cache:
            value = self.cache[key].value
            self.remove(key)
            self.add(key, value)
            return value

    def remove(self, key):

        next_node = self.cache[key].next
        prev_node = self.cache[key].prev

        if self.cache[key] == self.start_node:
            self.start_node = next_node

        if self.cache[key] == self.end_node:
            self.end_node = prev_node

        if prev_node: 
            prev_node.next = next_node

        if next_node: 
            next_node.prev = prev_node

        del self.cache[key]
        
    def print_state(self):
        ''' Print the current state of the cache '''
        print ('cache state', len(self.cache))
        iter_node = self.start_node
        while(iter_node):
            print (iter_node.key, iter_node.value)
            iter_node = iter_node.next

if __name__ == "__main__":
    lru_cache = LRU(3)
    inpt = [(1,2), (2,3), (3,4), (2,5)]

    for key, value in inpt:
        lru_cache.add(key,value)

    lru_cache.remove(2)
    
    
   

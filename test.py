from __future__ import print_function
from lru_cache import LRU

def print_state(lru_cache):
    print ('cache size', len(lru_cache.cache))
    iter_node = lru_cache.start_node
    while(iter_node):
        print ('key : ', iter_node.key, 'value : ', iter_node.value)
        iter_node = iter_node.next

if __name__ == "__main__":
    lru_cache = LRU(3)
    inpt = [(1,2), (2,3), (3,4), (2,5)]

    for key, value in inpt:
        lru_cache.add(key,value)

    print_state(lru_cache)
    lru_cache.remove(2)
    print_state(lru_cache)

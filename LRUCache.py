# LRUCache.py
# software library for question C

""" An LRU cache is used to remove the least recently used frame when the cache
is filled. If we reference an item that is in memory, we will need to detach the
node from the list and then move it to the front of the queue.To implement an LRU
cache we need two data structures:

1- A Doubly linked list (DLL) that will serve as a Queue. In a DLL, each node has
data and both a next and previous pointer. The maximum size of the queue  will
have a number of nodes equal to the cache size. The most recently used reference
will be near the front of the list(head) and the LRU reference will be placed near the
end (tail).

2- A key or hash to locate the corresponding queue entry and access its data.

If we reference an item that is in memory, we will need to detach the node from the
list and then move it to the front of the queue. If it is not in memory, we will add
it to the front of the list and remove the LRU reference and the end of the
queue if all nodes in the queue are already occupied. """

# import libraries
from datetime import datetime

# create a Node class
class Node:
    # Create a new node, by default all values will be set to None
    def __init__(self, key, data=None):
        self.key = key      # access the node using its key
        self.data = data    # data contained within the node
        self.next = None    # set the next pointer
        self.prev = None    # set the previous pointer
        self.timestamp = datetime.now() # add a timestamp for time expiration

class LRUCache:
    cache_limit = None
    verbose = False

    def __init__(self, func, time_delta=1):
        # set the number of nodes in the queue
        # set the function that will be using the cache decorator
        self.func = func
        # dictionary (or hash) holding the items in the cache
        self.cache = {}
        # maximum time an item can stay in the cache before it expires in seconds
        self.time_delta = time_delta

        # create the head (first) node and tail (last) node and link them together
        self.head = Node(key=0, data=0)
        self.tail = Node(key=0, data=0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __call__(self, *args, **kwargs):

        """We want to treat this instance of a class (aka Objects), as if if were a function: to achieve this we
        pass them to other methods/functions and call them. In order to achieve this, the __call__ class function
        has to be specialized. We want this function to be used as a decorator for another function. """

        # if the answer is in the cache, pull results from the queue and place the
        # newly accessed value at the head
        if args in self.cache:
            self._modifyQueue(args) # place new value at list head
            # print the cache to screen
            if self.verbose == True:
                print(f'Cached...{args}\n result: {self.cache[args]}\nCache: {self.cache}')
                # return the result saved in the cache
            return self.cache[args]

        # if the cache limit is exceeded:
        if self.cache_limit is not None:
            if len(self.cache) >= self.cache_limit:
                #remove the LRU item from the queue
                next = self.head.next
                self._remove(next)
                del self.cache[next.key]

        # if the value is not stored in the cache, compute the answer and store it
        result = self.func(*args, **kwargs)
        # create a node with the new argument and its data
        node = Node(key=args, data=result)
        self.cache[args] = result
        # add to the queue
        self._insert(node)
        if self.verbose == True:
            print(f'Result {result} added to cache on {node.timestamp.strftime("%b%d%Y %H:%M:%S")}\nCache: {self.cache}')
        return result

    """ Node manipulation functions """
    # insert the new node at the head of the list
    def _insert(self, node):
        # retrieve the node before the head, and set the node after it is as the
        # current node
        previous = self.tail.prev
        previous.next = node
        # link the node to the tail
        self.tail.prev = node
        # place the most recent node at the head before the previous node
        node.prev = previous
        node.next = self.tail

    # remove a node from the queue
    def _remove(self, node):
        # retrieve the node before and the node after
        previous = node.prev
        next = node.next
        # set the previous node to skip over to the next node (removing the one
        # in between), and vice versa
        previous.next = next
        next.prev = previous

    # if the result of the passed args is already in the queue, move it to the
    # head of the cache
    def _modifyQueue(self, args):
        # get the current head
        current = self.head
        while True:
            # check to see if that result exists in the queue
            if current.key == args:
                node = current
                # remove the node from its current position and then add it to the head
                self._remove(node)
                self._insert(node)

                # update the positions of the values in the cache
                del self.cache[node.key]
                self.cache[node.key] = node.data

                break

            else:
                # check the next node until a match is found
                current = current.next
                # check to see if the node has expired
                self._verifyNode(current)

    def _verifyNode(self, node):
        now = datetime.now()
        elapsed_time = (now-node.timestamp).seconds
        if elapsed_time > self.time_delta:
            if self.verbose == True:
                print(f"Warning: Node @ ({node.key}, {node.data}) has expired!")
        ### NOTE

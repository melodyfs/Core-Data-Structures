

# Double-ended queue
class ArrayDeque(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def push_front(self, item):
        """Insert the given item at the front of this queue.
        Running time: O(1) – appending an item at the front of list"""
        
        pass


    def push_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – appending an item at the end of list"""
        return self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list[0]

    def back(self):
        """Return the item at the back of the deque"""
        if self.is_empty():
            return None
        return self.list[len(self.list) - 1]


    def pop_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – removing the first item from list"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("Empty stack")
        return self.list.pop(0)

    def pop_back(self):
        """Remove and return the item at the back of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – removing the last item from list"""

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayDeque

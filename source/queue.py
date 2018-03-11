#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – appending an item at the end of linkedlist"""
        return self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – remove the first item of linkedlist"""
        if self.is_empty():
            raise ValueError("Empty queue")
        else:
            item = self.front()
            self.list.delete(item)
            return item

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.front_index = 0
        self.max_size = 4
        self.size = 0

        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.size == 0:
            return True
        return False


    def length(self):
        """Return the number of items in this queue."""
        return self.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – appending an item at the end of list"""

        # if self.front_index >= self.max_size:
        #     current_list = self.list
        #     self.list[self.front_index - self.max_size] = item
        # else:
        self.list.append(item)
        self.size += 1

    def resize():
        current_list = self.list
        self.list = []

        for index in range(self.max_size):
            self.list[index] = current_list[index + self.front_index]
        return self.list


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list[self.front_index]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – removing the first item from list"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("Empty stack")
        else:
            item = self.list[self.front_index]
            self.front_index += 1
            self.size -= 1
            return item

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
q = Queue(['A', 'B', 'C', 'D'])
q.dequeue()
q.dequeue()
q.dequeue()
print(q)
q.enqueue('X')
# print(q.list)
q.dequeue()
print(q) # 1

print(q.list)
q.enqueue('Y')
print(q)
# q.dequeue()
# print(q)
print(q.list)

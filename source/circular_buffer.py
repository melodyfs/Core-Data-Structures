
class CircularBuffer(object):

    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        '''Check if the buffer is empty. Return True if it is empty,
        False otherwise'''
        pass

    def is_full(self):
        '''Check if the buffer is full. Return True if it is full,
        False otherwise'''
        pass

    def enqueue(self, item):
        pass

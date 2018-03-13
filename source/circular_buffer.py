
class CircularBuffer(object):

    def __init__(self, max_size):
        self.list = list()
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        '''Check if the buffer is empty. Return True if it is empty,
        False otherwise'''
        if self.size == 0:
            return True
        return False

    def is_full(self):
        '''Check if the buffer is full. Return True if it is full,
        False otherwise'''
        if self.size == self.max_size:
            return True
        return False

    def enqueue(self, item):
        '''Insert item at the back of the buffer
        Running time: O(n-1)'''
        if self.is_full():
            self.list.pop()
            self.list.insert(0, item)
        else:
            self.list.append(item)
        self.size += 1

    def front(self):
        '''Return the item at the front of the buffer'''
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        '''Remove and return the item at the front of the buffer
        Running time: O(n-1)'''
        if self.is_empty():
            raise ValueError("Empty buffer")
        else:
            self.list.pop(0)
            self.size -= 1
            return self.front()


def test_cb():
    cb = CircularBuffer(3)
    cb.enqueue('A')
    cb.enqueue('B')
    cb.enqueue('C')
    print(cb.list)
    print('Front: ' + str(cb.front()))
    cb.enqueue('D')
    print(cb.list)
    print('Front: ' +  str(cb.front()))
    cb.dequeue()
    print(cb.list)
    print('Front: ' +  str(cb.front()))
    cb.enqueue('C')
    print(cb.list)
    cb.enqueue('E')
    print(cb.list)


if __name__ == '__main__':
    test_cb()

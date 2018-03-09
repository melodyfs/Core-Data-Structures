

class Set(object):

    def __init__(self, elements=None):
        self.size = 0
        self.list = list()

        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        '''Return True indicating the element is in this set. False otherwise'''
        return element in self.list

    def add(self, element):
        '''Add element to this set, if not present already'''
        if self.contains(element):
            raise ValueError("Element exists")
        else:
            self.list.append(element)
            self.size += 1

    def remove(self, element):
        '''Remove element from this set, if present, or else raise ValueError'''
        if self.contains(element):
            self.list.remove(element)
            self.size -= 1
        else:
            raise ValueError("Element not found")

    def union(self, other_set):
        '''Return a new set that is the union of this set and other_set'''
        # A new set initialized with current set
        new_set = Set(self.list)

        # Check whether elements from other set exists in new set
        for element in other_set.list:
            if not new_set.contains(element):
                new_set.add(element)
        return new_set

    def intersection(self, other_set):
        '''Return a new set that is the intersection of this set and other_set'''
        new_set = Set()

        for element in other_set.list:
            if self.contains(element):
                new_set.add(element)
        return new_set


    def difference(self, other_set):
        '''Return a new set that is the difference of this set and other_set'''
        # A new set initialized with current set
        new_set = Set(self.list)

        for element in other_set.list:
            if self.contains(element):
                new_set.remove(element)
            else:
                new_set.add(element)
        return new_set


    def is_subset(self, other_set):
        '''Return a boolean indicating whether other_set is a subset of this set'''
        for element in other_set.list:
            if self.contains(element):
                return True
            else:
                return False


def test_set():
    st = Set(['A', 'B', 'C'])
    # print(st.list)
    # st.remove('A')
    print("Current elements: " + str(st.list))
    print('Size: ' + str(st.size))
    st2 = Set(['D'])
    print(str(st2.list))
    print(str(st.intersection(st2).list))


if __name__ == '__main__':
    test_set()

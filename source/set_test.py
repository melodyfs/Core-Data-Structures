

from _set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        st = Set()
        assert st.size == 0
        assert st.list == []

    def test_init_with_list(self):
        st = Set(['A', 'B', 'C'])
        assert st.size == 3
        assert st.list == ['A', 'B', 'C']

    def test_contains(self):
        st = Set(['A', 'B', 'C'])
        assert st.contains('A') == True
        assert st.contains('B') == True
        assert st.contains('C') == True
        assert st.contains('D') == False

    def test_add(self):
        st = Set()
        st.add('A')
        assert st.size == 1
        st.add('B')
        assert st.size == 2
        st.add('C')
        assert st.size == 3
        with self.assertRaises(ValueError):
            st.add('B')

    def test_remove(self):
        st = Set(['A', 'B', 'C', 'D'])
        st.remove('A')
        assert st.size == 3
        st.remove('C')
        assert st.size == 2
        with self.assertRaises(ValueError):
            st.remove('A')

    def test_union(self):
        st = Set(['A', 'B', 'C', 'D'])
        st2 =  Set(['C', 'D', 'E','F'])
        union_with_overlapped = st.union(st2)
        assert union_with_overlapped.size == 6
        self.assertCountEqual(union_with_overlapped.list, ['A', 'B', 'C', 'D', 'E','F']) # Order doesn't matter
        st3 = Set(['X', 'Y', 'Z'])
        union_without_overlapped = st.union(st3)
        assert union_without_overlapped.size == 7
        self.assertCountEqual(union_without_overlapped.list, ['A', 'B', 'C', 'D', 'X', 'Y', 'Z'])

    def test_intersection(self):
        st = Set(['A', 'B', 'C', 'D'])
        st2 =  Set(['C', 'D', 'E','F'])
        intersection_true = st.intersection(st2)
        assert intersection_true.size == 2
        self.assertCountEqual(intersection_true.list, ['C', 'D'])
        st3 = Set(['X', 'Y', 'Z'])
        intersection_false = st.intersection(st3)
        assert intersection_false.size == 0
        assert intersection_false.list == []

    def test_difference(self):
        st = Set(['A', 'B', 'C', 'D'])
        st2 =  Set(['C', 'D', 'E','F'])
        difference_true = st.difference(st2)
        assert difference_true.size == 4
        self.assertCountEqual(difference_true.list, ['A', 'B', 'E', 'F'])
        st3 = Set(['A', 'B', 'C', 'D'])
        difference_false = st.difference(st3)
        assert difference_false.size == 0
        assert difference_false.list == []

    def test_is_subset(self):
        st = Set(['A', 'B', 'C', 'D'])
        st2 =  Set(['C', 'D', 'E','F'])
        assert st.is_subset(st2) == True
        st3 = Set(['X', 'Y', 'Z'])
        assert st.is_subset(st3) == False


if __name__ == '__main__':
    unittest.main()

#!python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        if self.is_leaf():
            return 0
        # Check if right child has a value and if so calculate its height
        right_h = 0
        if self.right is not None:
            right_h = self.right.height()
        # Check if left child has a value and if so calculate its height
        left_h = 0
        if self.left is not None:
            left_h = self.left.height()
        # Return one more than the greater of the left height and right height
        return max(left_h, right_h) + 1


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # Check if root node has a value and if so calculate its height
        if self.is_empty():
            return 0
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        O(h) ~= log base2
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():

            #  Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            #  Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        #  Check if the given item should be inserted right of parent node
        elif item > parent.data:
            #  Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data is item:
                # Return the found node
                return node
            #  Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            #  Check if the given item is greater than the node's data
            else: # item > node.data
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item is node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            #  Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item is node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                #  Update the parent and descend to the node's left child
                parent = node
                node = node.left
            #  Check if the given item is greater than the node's data
            else: #item > node.data
                # Update the parent and descend to the node's right child
                parent = node
                node = node.left
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        elif item is node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def _find_successor(self, node):
        '''Find successor for node when deleting a node with 2 children --
        retrieve the min value from the node's right subtree'''

        # while node.right.is_empty() is False
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current


        # current = self.root
        # successor = None
        # while current:
        #     if node.data > current.data:
        #         current = current.right
        #     elif node.data < current.data:
        #         successor = current
        #         current = current.left
        #     else:
        #         break
        # return successor



    def delete(self, item, parent=None):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

        # if node not self.root:
        parent = self._find_parent_node_recursive(item, self.root)
        node = self._find_node_iterative(item)

        if node is self.root:
            parent = self.root
            node = self.root
            print("parent")


        # Case 1: node doesn't have children
        if not node.right and not node.left:
            node = None
            print('node none')
            return node
        # Case 2: node has 2 children
        if node.right and node.left:
            successor = self._find_successor(node)
            succ_data = successor.data
            node.data = succ_data
            print('successor: ' + str(successor))
            print('succ data: ' + str(succ_data))
            # print('node data: ' + str(node.data))
            if succ_data < item:
                self.delete(succ_data, node.left)
            elif succ_data > item:
                self.delete(succ_data, node.right)

        # Case 3: node has 1 child
        if node.right and not node.left:
            if parent.right is node:
                parent.right = node.right
            elif parent.left is node:
                parent.left = node.right
            node = None
        elif not node.right and node.left:
            if parent.right is node:
                parent.right = node.left
            elif parent.left is node:
                parent.left = node.left
            node = None


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions?
        TODO: Memory usage: O(h) ~= log base2 of n Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Visit this node's data with given function
        visit(node.data)
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions?
        TODO: Memory usage: O(n/2) Why and under what conditions?"""
        # Create queue to store nodes not yet traversed in level-order
        from queue import LinkedQueue
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while queue.is_empty() is False:
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        # print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))
    #
    # print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))
    # print(tree.root.height())
    #
    # print('\nTraversing items:')
    # print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))
    tree.delete(2)
    print('\ntree root: ' + str(tree.root))
    print('tree left: ' + str(tree.root.left))
    print('tree right: ' + str(tree.root.right))





if __name__ == '__main__':
    test_binary_search_tree()

from typing import Generic, Iterator, Optional, TypeVar
from .BinaryTree import BinaryTree, Node # Correctly import the base classes

T = TypeVar('T') # The type T is expected to support <, >, and ==

class BinarySearchTree(BinaryTree[T], Generic[T]):
    """
    A Binary Search Tree (BST) implementation.
    """
    def __init__(self, root: Optional[Node[T]] = None) -> None:
        super().__init__(root)

    def add(self, value: T) -> None:
        """Adds a value to the BST, maintaining the BST property."""
        if not self._root:
            self._root = Node(value)
            return

        current = self._root
        while True:
            if value < current.data:  # type: ignore
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:  # value >= current.data, duplicates go to the right
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def __contains__(self, value: T) -> bool:
        """
        Checks if a value exists in the tree.
        """
        current = self._root
        while current:
            if value == current.data:
                return True
            if value < current.data: # type: ignore
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value: T) -> None:
        """Deletes a value from the tree, maintaining the BST property."""
        self._root = self._delete_recursive(self._root, value)

    def _delete_recursive(self, node: Optional[Node[T]], value: T) -> Optional[Node[T]]:
        """Recursively finds and deletes the node with the given value."""
        if node is None:
            return None

        if value < node.data: # type: ignore
            node.left = self._delete_recursive(node.left, value)
            return node
        if value > node.data: # type: ignore
            node.right = self._delete_recursive(node.right, value)
            return node

        # --- Node found, handle deletion cases ---
        # Case 1: Node has no left child
        if node.left is None:
            return node.right
        
        # Case 2: Node has no right child
        if node.right is None:
            return node.left

        # Case 3: Node has two children
        # Find the in-order successor (smallest node in the right subtree)
        successor_node = self._find_min(node.right)
        # Replace node's data with successor's data
        node.data = successor_node.data
        # Delete the successor from the right subtree
        node.right = self._delete_recursive(node.right, successor_node.data)
        return node

    def _find_min(self, node: Node[T]) -> Node[T]:
        """Finds the node with the minimum value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def _find_max(self, node: Node[T]) -> Node[T]:
        """Finds the node with the maximum value in a subtree."""
        current = node
        while current.right:
            current = current.right
        return current
        
    def _find_node(self, start_node: Optional[Node[T]], value: T) -> Optional[Node[T]]:
        """Finds the node containing the given value."""
        current = start_node
        while current:
            if value == current.data:
                return current
            if value < current.data: # type: ignore
                current = current.left
            else:
                current = current.right
        return None

    def successor(self, value: T) -> Optional[T]:
        """Finds the in-order successor of a given value in the tree."""
        target_node = self._find_node(self._root, value)
        if not target_node:
            return None # Value not in tree

        # Case 1: Node has a right subtree, successor is the min of that subtree
        if target_node.right:
            return self._find_min(target_node.right).data

        # Case 2: No right subtree, successor is the lowest ancestor for which
        # the target_node is in its left subtree.
        successor = None
        ancestor = self._root
        while ancestor and ancestor != target_node:
            if target_node.data < ancestor.data: # type: ignore
                successor = ancestor # This ancestor is a potential successor
                ancestor = ancestor.left
            else: # target_node.data > ancestor.data
                ancestor = ancestor.right
        
        return successor.data if successor else None

    def predecessor(self, value: T) -> Optional[T]:
        """Finds the in-order predecessor of a given value in the tree."""
        target_node = self._find_node(self._root, value)
        if not target_node:
            return None # Value not in tree

        # Case 1: Node has a left subtree, predecessor is the max of that subtree
        if target_node.left:
            return self._find_max(target_node.left).data

        # Case 2: No left subtree, predecessor is the lowest ancestor for which
        # the target_node is in its right subtree.
        predecessor = None
        ancestor = self._root
        while ancestor and ancestor != target_node:
            if target_node.data > ancestor.data: # type: ignore
                predecessor = ancestor # This ancestor is a potential predecessor
                ancestor = ancestor.right
            else: # target_node.data < ancestor.data
                ancestor = ancestor.left
        
        return predecessor.data if predecessor else None

    def __iter__(self) -> Iterator[T]:
        """The default iterator for the tree is in-order."""
        return self.inorder()

    def __len__(self) -> int:
        """Returns the total number of nodes in the tree."""
        return self._count_nodes(self._root)
    
    def _count_nodes(self, node: Optional[Node[T]]) -> int:
        """Recursively counts the nodes in a subtree."""
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def __str__(self) -> str:
        """Returns the canonical string representation of the tree."""
        return self.get_canonical_representation()

def test_BST():
    """A comprehensive test suite for the BinarySearchTree class."""
    print("--- Running BST Test Suite ---")
    
    bst = BinarySearchTree[int]()
    
    # Test adding
    values_to_add = [10, 5, 15, 2, 7, 12, 18, 1, 3, 6, 8]
    for v in values_to_add:
        bst.add(v)
    
    print(f"Tree after adding {len(values_to_add)} elements: {bst}")
    assert len(bst) == 11
    
    # Test __contains__ and inorder traversal (which should be sorted)
    print("In-order traversal:", list(bst.inorder()))
    assert list(bst.inorder()) == sorted(values_to_add)
    assert (10 in bst) is True
    assert (7 in bst) is True
    assert (99 in bst) is False

    # Test successor and predecessor
    print(f"Successor of 7: {bst.successor(7)}")
    assert bst.successor(7) == 8
    print(f"Predecessor of 7: {bst.predecessor(7)}")
    assert bst.predecessor(7) == 6
    print(f"Successor of 10: {bst.successor(10)}")
    assert bst.successor(10) == 12
    print(f"Predecessor of 10: {bst.predecessor(10)}")
    assert bst.predecessor(10) == 8
    print(f"Successor of 18 (max element): {bst.successor(18)}")
    assert bst.successor(18) is None
    print(f"Predecessor of 1 (min element): {bst.predecessor(1)}")
    assert bst.predecessor(1) is None

    # Test deletion
    # Case 1: Delete a leaf node (3)
    bst.delete(3)
    print(f"\nAfter deleting leaf node 3: {bst}")
    assert (3 in bst) is False
    assert len(bst) == 10
    assert list(bst.inorder()) == [1, 2, 5, 6, 7, 8, 10, 12, 15, 18]

    # Case 2: Delete a node with one child (18)
    bst.delete(18) # 18 has no children, so it's also a leaf
    print(f"After deleting node 18: {bst}")
    assert (18 in bst) is False
    assert len(bst) == 9
    assert list(bst.inorder()) == [1, 2, 5, 6, 7, 8, 10, 12, 15]

    # Case 3: Delete a node with two children (5)
    bst.delete(5)
    print(f"After deleting node 5: {bst}")
    assert (5 in bst) is False
    assert len(bst) == 8
    # The successor of 5 was 6, so 6 should replace it.
    assert list(bst.inorder()) == [1, 2, 6, 7, 8, 10, 12, 15]

    # Case 4: Delete the root node (10)
    bst.delete(10)
    print(f"After deleting root node 10: {bst}")
    assert (10 in bst) is False
    assert len(bst) == 7
    # The successor of 10 was 12, so 12 should be the new root.
    assert list(bst.inorder()) == [1, 2, 6, 7, 8, 12, 15]
    
    print("\n--- BST Test Suite Passed! ---")

def main():
    test_BST()

if __name__ == "__main__":
    main()

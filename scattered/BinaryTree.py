from typing import Generic, Iterator, Optional, Self, TypeVar
from collections import deque

T = TypeVar('T')

"""
A Binary Tree implementation supporting various traversals.
Note: The comments in this file are AI-generated.
"""

class Node(Generic[T]):
    """Represents a single node in a binary tree."""
    def __init__(self, data: T, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        # Note: This can cause a RecursionError for very deep trees.
        # It's suitable for simple representations.
        return f"Node(data={repr(self.data)})"

class BinaryTree(Generic[T]):
    """
    A Binary Tree implementation supporting various traversals.
    """
    def __init__(self, root: Optional[Node[T]] = None) -> None:
        self._root = root

    def inorder(self) -> Iterator[T]:
        """Yields nodes in In-order (Left, Root, Right)."""
        yield from self._inorder(self._root)

    def _inorder(self, node: Optional[Node[T]]) -> Iterator[T]:
        if node:
            yield from self._inorder(node.left)
            yield node.data
            yield from self._inorder(node.right)

    def preorder(self) -> Iterator[T]:
        """Yields nodes in Pre-order (Root, Left, Right)."""
        yield from self._preorder(self._root)

    def _preorder(self, node: Optional[Node[T]]) -> Iterator[T]:
        if node:
            yield node.data
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def postorder(self) -> Iterator[T]:
        """Yields nodes in Post-order (Left, Right, Root)."""
        yield from self._postorder(self._root)

    def _postorder(self, node: Optional[Node[T]]) -> Iterator[T]:
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.data

    def print_inorder(self) -> None:
        """Prints all node data in-order on a single line."""
        print(" ".join(map(str, self.inorder())))

    def print_preorder(self) -> None:
        """Prints all node data pre-order on a single line."""
        print(" ".join(map(str, self.preorder())))

    def print_postorder(self) -> None:
        """Prints all node data post-order on a single line."""
        print(" ".join(map(str, self.postorder())))

    def print_level_order(self) -> None:
        """Prints the tree level by level."""
        if not self._root:
            return

        queue = deque([self._root])
        while queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                node: Node = queue.popleft()
                current_level_values.append(str(node.data))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(" ".join(current_level_values))

    def get_canonical_representation(self) -> str:
        """
        Returns the canonical string representation of the tree.
        Format: "(<root_data><left_subtree><right_subtree>)"
        """
        return self._canonicalize(self._root)

    def _canonicalize(self, node: Optional[Node[T]]) -> str:
        if node is None:
            return ""
        # Using repr() for node.data to handle strings vs. numbers correctly
        return f"({repr(node.data)}{self._canonicalize(node.left)}{self._canonicalize(node.right)})"

    def __iter__(self) -> Iterator[T]:
        """The default iterator for the tree is in-order."""
        return self.inorder()
    
    def __repr__(self) -> str:
        # Note: This can cause a RecursionError for very deep trees.
        # It's suitable for simple representations.
        return f"BinaryTree(root={repr(self._root)})"

    def __str__(self) -> str:
        """The default string representation for the tree is the canonical representation."""
        return self.get_canonical_representation()

    def __len__(self) -> int:
        """Returns the number of nodes in the tree."""
        return self._count_nodes(self._root)

    def _count_nodes(self, node: Optional[Node[T]]) -> int:
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def __contains__(self, value: T) -> bool:
        """Allows for checking if a value is in the tree (e.g., value in tree)."""
        return self._contains(self._root, value)

    def _contains(self, node: Optional[Node[T]], value: T) -> bool:
        if node is None:
            return False
        if node.data == value:
            return True
        return self._contains(node.left, value) or self._contains(node.right, value)

    def __eq__(self, other: object) -> bool:
        """Allows for checking if two trees are equal (e.g., tree1 == tree2)."""
        if not isinstance(other, BinaryTree):
            return False
        return self.get_canonical_representation() == other.get_canonical_representation()
    

def test_binary_tree():
    tree = BinaryTree[int]()
    assert len(tree) == 0
    assert not tree
    assert repr(tree) == "BinaryTree(root=None)"

    # Create nodes
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(3)
    root_node.left.left = Node(4)
    root_node.left.right = Node(5)
    root_node.right.right = Node(6)

    # Create the tree
    tree = BinaryTree(root_node)

    assert len(tree) == 6
    assert bool(tree)
    assert str(tree) == "(1(2(4)(5))(3(6)))"
 
    assert 1 in tree
    assert 7 not in tree

    assert " ".join(map(str, tree.postorder())) == "4 5 2 6 3 1"
    assert " ".join(map(str, tree.inorder())) == "4 2 5 1 3 6"
    assert " ".join(map(str, tree.preorder())) == "1 2 4 5 3 6"

    print("All tests passed BinaryTree < :)")


if __name__ == "__main__":
    test_binary_tree()
    
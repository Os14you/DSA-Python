from typing import Generic, Iterator, Optional, TypeVar, Protocol

class Comparable(Protocol):
    """Protocol for types that support comparison operations."""
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...

T = TypeVar('T', bound=Comparable)

class AVLNode(Generic[T]):
    """A node in an AVL tree with automatic height management."""
    
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.height: int = 0
        self.left: Optional['AVLNode[T]'] = None
        self.right: Optional['AVLNode[T]'] = None
    
    def __repr__(self) -> str:
        return f"AVLNode(data={self.data}, height={self.height})"
    
    def __str__(self) -> str:
        return f"AVLNode(data={self.data}, height={self.height})"
    
    @staticmethod
    def get_height(node: Optional['AVLNode[T]']) -> int:
        """Get the height of a node, returning -1 for None."""
        return node.height if node is not None else -1
    
    def update_height(self) -> None:
        """Update the height of this node based on its children."""
        left_height = self.get_height(self.left)
        right_height = self.get_height(self.right)
        self.height = 1 + max(left_height, right_height)

    def get_balance_factor(self) -> int:
        """Calculate the balance factor (left height - right height)."""
        left_height = self.get_height(self.left)
        right_height = self.get_height(self.right)
        return left_height - right_height

class AVLTree(Generic[T]):
    """A self-balancing binary search tree (AVL Tree) implementation."""
    
    def __init__(self) -> None:
        self._root: Optional[AVLNode[T]] = None
        self._size: int = 0
    
    @property
    def size(self) -> int:
        """Return the number of elements in the tree."""
        return self._size
    
    @property
    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self._root is None
    
    def _rotate_left(self, node: AVLNode[T]) -> AVLNode[T]:
        """
        Perform a left rotation on the given node.
        
        Args:
            node: The node to rotate left around.
            
        Returns:
            The new root of the rotated subtree.
        """
        if node.right is None:
            raise ValueError("Cannot perform left rotation: right child is None")
        
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        # Update heights (order matters: update lower nodes first)
        node.update_height()
        new_root.update_height()
        
        return new_root

    def _rotate_right(self, node: AVLNode[T]) -> AVLNode[T]:
        """
        Perform a right rotation on the given node.
        
        Args:
            node: The node to rotate right around.
            
        Returns:
            The new root of the rotated subtree.
        """
        if node.left is None:
            raise ValueError("Cannot perform right rotation: left child is None")
        
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        # Update heights (order matters: update lower nodes first)
        node.update_height()
        new_root.update_height()
        
        return new_root
    
    def _balance_node(self, node: AVLNode[T]) -> AVLNode[T]:
        """
        Balance a node if it's unbalanced.
        
        Args:
            node: The node to potentially balance.
            
        Returns:
            The root of the balanced subtree.
        """
        balance_factor = node.get_balance_factor()
        
        # Left heavy cases
        if balance_factor > 1:
            if node.left is not None and node.left.get_balance_factor() < 0:
                # Left-Right case
                node.left = self._rotate_left(node.left)
            # Left-Left case
            return self._rotate_right(node)
        
        # Right heavy cases
        if balance_factor < -1:
            if node.right is not None and node.right.get_balance_factor() > 0:
                # Right-Left case
                node.right = self._rotate_right(node.right)
            # Right-Right case
            return self._rotate_left(node)
        
        return node
    
    def _insert_recursive(self, node: Optional[AVLNode[T]], value: T) -> AVLNode[T]:
        """
        Recursively insert a value into the subtree rooted at node.
        
        Args:
            node: The root of the current subtree.
            value: The value to insert.
            
        Returns:
            The root of the modified subtree.
        """
        # Base case: create new node
        if node is None:
            self._size += 1
            return AVLNode(value)
        
        # Recursive insertion
        if value < node.data:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.data:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Value already exists, no insertion needed
            return node
        
        # Update height and rebalance
        node.update_height()
        return self._balance_node(node)
    
    def insert(self, value: T) -> None:
        """Insert a value into the AVL tree."""
        self._root = self._insert_recursive(self._root, value)
    
    def _find_min_node(self, node: AVLNode[T]) -> AVLNode[T]:
        """Find the node with the minimum value in the given subtree."""
        while node.left is not None:
            node = node.left
        return node
    
    def _remove_recursive(self, node: Optional[AVLNode[T]], value: T) -> Optional[AVLNode[T]]:
        """
        Recursively remove a value from the subtree rooted at node.
        
        Args:
            node: The root of the current subtree.
            value: The value to remove.
            
        Returns:
            The root of the modified subtree, or None if subtree becomes empty.
        """
        if node is None:
            return None
        
        # Find the node to remove
        if value < node.data:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.data:
            node.right = self._remove_recursive(node.right, value)
        else:
            # Found the node to remove
            self._size -= 1
            
            # Case 1: Node has no children or only right child
            if node.left is None:
                return node.right
            
            # Case 2: Node has only left child
            if node.right is None:
                return node.left
            
            # Case 3: Node has both children
            # Replace with inorder successor (minimum in right subtree)
            min_node = self._find_min_node(node.right)
            node.data = min_node.data
            node.right = self._remove_recursive(node.right, min_node.data)
            # Note: we don't decrement _size here since it was already decremented above
            self._size += 1  # Compensate for the extra decrement that will happen
        
        # Update height and rebalance
        node.update_height()
        return self._balance_node(node)
    
    def remove(self, value: T) -> bool:
        """
        Remove a value from the AVL tree.
        
        Args:
            value: The value to remove.
            
        Returns:
            True if the value was found and removed, False otherwise.
        """
        original_size = self._size
        self._root = self._remove_recursive(self._root, value)
        return self._size < original_size
    
    def _search_recursive(self, node: Optional[AVLNode[T]], value: T) -> bool:
        """Recursively search for a value in the subtree."""
        if node is None:
            return False
        
        if value == node.data:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def contains(self, value: T) -> bool:
        """Check if a value exists in the tree."""
        return self._search_recursive(self._root, value)
    
    def _inorder_recursive(self, node: Optional[AVLNode[T]]) -> Iterator[T]:
        """Generate values in inorder traversal."""
        if node is not None:
            yield from self._inorder_recursive(node.left)
            yield node.data
            yield from self._inorder_recursive(node.right)
    
    def inorder_traversal(self) -> Iterator[T]:
        """Return an iterator for inorder traversal of the tree."""
        return self._inorder_recursive(self._root)
    
    def to_list(self) -> list[T]:
        """Return a sorted list of all values in the tree."""
        return list(self.inorder_traversal())
    
    def _validate_avl_recursive(self, node: Optional[AVLNode[T]]) -> tuple[bool, int]:
        """
        Validate that the subtree rooted at node is a valid AVL tree.
        
        Returns:
            A tuple of (is_valid, height)
        """
        if node is None:
            return True, -1
        
        # Recursively validate children
        left_valid, left_height = self._validate_avl_recursive(node.left)
        right_valid, right_height = self._validate_avl_recursive(node.right)
        
        if not left_valid or not right_valid:
            return False, 0
        
        # Check height calculation
        expected_height = 1 + max(left_height, right_height)
        if node.height != expected_height:
            return False, 0
        
        # Check balance factor
        balance_factor = left_height - right_height
        if abs(balance_factor) > 1:
            return False, 0
        
        return True, expected_height
    
    def is_valid_avl(self) -> bool:
        """Check if the tree maintains AVL properties."""
        valid, _ = self._validate_avl_recursive(self._root)
        return valid
    
    def __len__(self) -> int:
        """Return the number of elements in the tree."""
        return self._size
    
    def __bool__(self) -> bool:
        """Return True if the tree is not empty."""
        return not self.is_empty
    
    def __contains__(self, value: T) -> bool:
        """Support 'in' operator."""
        return self.contains(value)
    
    def __iter__(self) -> Iterator[T]:
        """Support iteration over the tree in sorted order."""
        return self.inorder_traversal()
    
    def __repr__(self) -> str:
        """Return a string representation of the tree."""
        if self.is_empty:
            return "AVLTree([])"
        return f"AVLTree({self.to_list()})"
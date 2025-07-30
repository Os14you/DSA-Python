from typing import Generic, Iterator, Optional, Self, TypeVar

"""
A linked list implementation in Python.
Note: The comments in this file are AI-generated.
"""
T = TypeVar('T')

class Node(Generic[T]):
    """
    A single node in a linked list.

    Attributes:
        data (T): The data stored in the node.
        next (Optional[Node[T]]): A pointer to the next node in the list.
    """
    def __init__(self, data: T, next_node: Optional[Self] = None) -> None:
        self.data = data
        self.next = next_node

    def __repr__(self) -> str:
        """Provides a developer-friendly representation of the node."""
        return f"Node({self.data})"


class LinkedList(Generic[T]):
    """
    A singly linked list implementation.

    This data structure consists of a sequence of nodes, where each node
    points to the next one. It provides O(1) time complexity for insertions
    at the head or tail.
    """
    def __init__(self) -> None:
        """Initializes an empty linked list."""
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.__len = 0

    def insert_front(self, value: T) -> None:
        """
        Inserts a new node with the given value at the head of the list.

        Time Complexity: O(1)
        """
        new_node = Node(value, self.head)
        self.head = new_node

        # If the list was empty, the new node is also the tail.
        if self.tail is None:
            self.tail = new_node

        self.__len += 1

    def insert_end(self, value: T) -> None:
        """
        Inserts a new node with the given value at the tail of the list.

        Time Complexity: O(1)
        """
        # If the list is empty, inserting at the end is the same as the front.
        if self.head is None:
            self.insert_front(value)
            return

        # This assertion helps the type checker understand that if we reach
        # this point, 'self.tail' cannot be None.
        assert self.tail is not None, "Tail should not be None if head is not None"

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.__len += 1

    def delete_front(self) -> None:
        """
        Removes the node from the head of the list.

        Time Complexity: O(1)
        """
        if self.head is None:
            return

        self.head = self.head.next
        self.__len -= 1

        # If the list became empty after deletion, update the tail as well.
        if self.head is None:
            self.tail = None

    def delete_end(self) -> None:
        """
        Removes the node from the tail of the list.

        Time Complexity: O(n) because we must traverse to find the new tail.
        """
        if self.head is None:
            return

        # If there's only one element, deleting the end is the same as the front.
        if self.head.next is None:
            self.delete_front()
            return

        # Traverse until we find the second-to-last node.
        current = self.head
        while current.next and current.next.next:
            current = current.next

        # Unlink the last node and update the tail.
        current.next = None
        self.tail = current
        self.__len -= 1

    def get(self, index: int) -> T:
        """
        Returns the value of the node at the given index.
        Time Complexity: O(n) because we must traverse to find the node.
        """

        if not (0 <= index < self.__len) or self.head is None:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            # This assertion helps the type checker understand that if we reach
            # this point, 'current' cannot be None.
            assert current is not None
            current = current.next

        assert current is not None, "Current should not be None if index is valid"

        return current.data

    def delete(self, index: int) -> None:
        """
        Deletes the node at the given index.
        Time Complexity: O(n) because we must traverse to find the node.
        """

        if not (0 <= index < self.__len) or self.head is None:
            raise IndexError("Index out of range")

        if index == 0:
            self.delete_front()
            return

        current = self.head
        for _ in range(index - 1):
            assert current is not None
            current = current.next

        assert current is not None, "Current should not be None if index is valid"
        current.next = current.next.next # type: ignore cause current->next could be None
        self.__len -= 1

    def __len__(self) -> int:
        """Returns the number of nodes in the list. Time Complexity: O(1)"""
        return self.__len

    def __iter__(self) -> Iterator[T]:
        """Allows for iterating over the list's data (e.g., in a for loop)."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """Provides a developer-friendly representation of the linked list."""
        if self.head is None:
            return "LinkedList()"
        
        # Use the iterator to build a string representation
        return f"LinkedList({ ' -> '.join(map(str, self)) })"
    
    def __getitem__(self, index: int) -> T:
        """Allows for indexing into the list (e.g., list[index])."""
        return self.get(index)

def test_linked_list():
    ll = LinkedList()
    ll.insert_front(1)
    ll.insert_front(2)
    ll.insert_front(3)
    ll.insert_end(4)

    assert ll.get(0) == 3
    assert ll.get(1) == 2
    assert ll.get(2) == 1
    assert ll.get(3) == 4

    ll.delete_front()
    assert ll.get(0) == 2
    assert ll.get(1) == 1
    assert ll.get(2) == 4

    ll.delete_end()
    assert ll.get(0) == 2
    assert ll.get(1) == 1

    ll.delete(1)
    assert ll.get(0) == 2

    print("All tests passed [Linked->List]! :)")

if __name__ == "__main__":
    test_linked_list()
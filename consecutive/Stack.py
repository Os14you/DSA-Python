from collections import deque
from typing import TypeVar, Generic, Iterator

# Define a generic TypeVar
T = TypeVar('T')

class Stack(Generic[T]):
    """
    A generic Stack implementation using collections.deque.
    """
    def __init__(self) -> None:
        self._container: deque[T] = deque()

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""
        self._container.append(item)

    def pop(self) -> T:
        """
        Removes and returns the item from the top of the stack.
        Raises IndexError if the stack is empty.
        """
        return self._container.pop()

    def __iter__(self) -> Iterator[T]:
        """Provides an iterator from bottom to top of the stack."""
        return iter(self._container)

    def __len__(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._container)

    def __repr__(self) -> str:
        """
        Provides an unambiguous string representation of the stack,
        showing contents from bottom to top.
        e.g., Stack(deque(['a', 'b', 'c']))
        """
        return f"Stack({self._container})"
    
    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the stack,
        formatted to show items from top to bottom.
        e.g., Stack[c, b, a ->
        """
        if not self._container:
            return "Stack[ ->"
            
        # Create a comma-separated string of the items in reverse (top-to-bottom) order
        items_str = ", ".join(map(str, self._container))
        
        # Return the final formatted string
        return f"Stack[{items_str} ->"
    
    def __bool__(self) -> bool:
        """Returns True if the stack is not empty, False otherwise."""
        return bool(self._container)

    def __contains__(self, item: T) -> bool:
        """Checks if an item is in the stack."""
        return item in self._container

def test_stack():
    stack = Stack()
    assert not stack

    stack.push(1)
    stack.push(2)
    assert stack
    assert stack.pop() == 2
    assert stack.pop() == 1

    stack.push(3)
    stack.push(4)
    assert len(stack) == 2
    assert 3 in stack

    assert str(stack) == "Stack[3, 4 ->"

    print("All tests passed [Stack ! :)")

if __name__ == "__main__":
    test_stack()
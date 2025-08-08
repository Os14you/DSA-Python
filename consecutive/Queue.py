from collections import deque
from typing import TypeVar, Generic, Iterator

# Define a generic TypeVar to allow the Queue to hold any type of element.
T = TypeVar('T')

class Queue(Generic[T]):
    """
    A generic First-In-First-Out (FIFO) queue implementation.
    
    This class uses collections.deque for efficient appends and pops
    from both ends of the underlying data structure.
    """
    def __init__(self) -> None:
        """Initializes an empty queue."""
        self._container: deque[T] = deque()

    def push(self, val: T) -> None:
        """Adds an element to the back of the queue."""
        self._container.appendleft(val)
    
    def pop(self) -> T:
        """
        Removes and returns the element from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        return self._container.pop()

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator for the queue's elements."""
        return iter(self._container)

    def __str__(self) -> str:
        """Returns an informal, user-friendly string representation of the queue."""
        if not self._container:
            return "Queue -> ( ) ->"
        items_str = ", ".join(map(str, reversed(self._container)))
        return f"Queue -> ({items_str}) ->"
    
    def __len__(self) -> int:
        """Returns the number of items in the queue."""
        return len(self._container)

    def __bool__(self) -> bool:
        """Returns True if the queue is not empty, False otherwise."""
        return bool(self._container)

    def __contains__(self, item: T) -> bool:
        """Checks if an item is present in the queue."""
        return item in self._container
    
    def __repr__(self) -> str:
        """Returns a formal, unambiguous string representation of the Queue object."""
        return f"Queue({self._container})"


def test_queue():
    """
    Tests all functionalities of the Queue class using assertions.
    Prints a success message only if all tests pass.
    """
    # 1. Test empty queue initialization
    q = Queue[int]()
    assert len(q) == 0
    assert not q
    assert str(q) == "Queue -> ( ) ->"
    assert repr(q) == "Queue(deque([]))"

    # 2. Test push operation
    q.push(10)
    q.push(20)
    q.push(30)
    assert len(q) == 3
    assert bool(q)
    assert str(q) == "Queue -> (10, 20, 30) ->"

    # 3. Test __contains__
    assert 20 in q
    assert 99 not in q

    # 4. Test __iter__
    # The iterator yields items in the deque's internal order (LIFO)
    iterator = iter(q)
    assert next(iterator) == 30
    assert next(iterator) == 20
    assert next(iterator) == 10

    # 5. Test pop operation
    assert q.pop() == 10
    assert len(q) == 2
    assert str(q) == "Queue -> (20, 30) ->"
    
    assert q.pop() == 20
    assert len(q) == 1

    # 6. Test popping the last item
    assert q.pop() == 30
    assert len(q) == 0
    assert not q

    # 7. Test popping from an empty queue (should raise IndexError)
    try:
        q.pop()
        # If this line is reached, the test fails because no exception was raised
        assert False, "IndexError was not raised for pop() on an empty queue"
    except IndexError:
        # This is the expected behavior, so we pass
        pass

    # 8. Test with a different type (string)
    q_str = Queue[str]()
    q_str.push("hello")
    q_str.push("world")
    assert len(q_str) == 2
    assert "hello" in q_str
    assert q_str.pop() == "hello"
    assert repr(q_str) == "Queue(deque(['world']))"
    
    print("All tests passed -> Queue -> ! :)")


if __name__ == "__main__":
    test_queue()
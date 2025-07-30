from .LinkedList import LinkedList, test_linked_list
from .Stack import Stack, test_stack
from .Queue import Queue, test_queue

__all__ = ["LinkedList", "Stack", "Queue"]
__version__ = "0.3.1"

def main():
    test_linked_list()
    test_stack()
    test_queue()

if __name__ == "__main__":
    print(f"Scattered [v{__version__}]")
    main()
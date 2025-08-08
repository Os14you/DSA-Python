from .Queue import Queue, test_queue
from .Stack import Stack, test_stack

__all__ = ["Stack", "Queue"]
__version__ = "0.1.0"

def main():
    test_stack()
    test_queue()

if __name__ == "__main__":
    print(f"Consecutive [v{__version__}]")
    main()
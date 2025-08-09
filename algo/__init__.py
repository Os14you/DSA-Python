from .sort import insertionSort, test_insert_sort

__all__ = []
__version__ = "0.1.0"

def main():
    print(f"Algo [v{__version__}]")
    
    test_insert_sort()

if __name__ == "__main__":
    main()
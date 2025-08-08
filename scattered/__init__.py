from .LinkedList import LinkedList, test_linked_list
from .BinaryTree import BinaryTree, test_binary_tree
from .BinarySearchTree import BinarySearchTree, test_BST

__all__ = ["LinkedList", "BinaryTree", "BinarySearchTree"]
__version__ = "0.4.1"

def main():
    test_linked_list()
    test_binary_tree()
    test_BST()

if __name__ == "__main__":
    print(f"Scattered [v{__version__}]")
    main()
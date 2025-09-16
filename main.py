from scattered import test_linked_list, test_binary_tree, test_BST
from consecutive import test_queue, test_stack
from algo import test_insert_sort, test_bubble_sort

def main():
    test_linked_list()
    test_stack()
    test_queue()
    test_binary_tree()
    test_BST()
    test_insert_sort()
    test_bubble_sort()

if __name__ == "__main__":
    main()
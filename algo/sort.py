def insertionSort(lst: list) -> None:
    """
    Sorts a list using the insertion sort algorithm.
    
    :param list: A list of elements to be sorted.
    """
    for i in range(len(lst)):
        element, j = lst[i], i - 1

        while j >= 0 and lst[j] > element:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = element

def test_insert_sort() -> None:
    """
    Tests the insertion sort function with a sample list.
    
    :return: None
    """
    sample_list = [5, 2, 9, 1, 5, 6]
    insertionSort(sample_list)
    assert sample_list == [1, 2, 5, 5, 6, 9], "Insertion sort failed"
    print("Insertion sort passed!!")

def bubbleSort(lst: list) -> None:
    """
    Sorts a list using the bubble sort algorithm.
    
    :param list: A list of elements to be sorted.
    """
    for amount_shifts in range(len(lst)):
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                swapped = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if not swapped:
            break

def test_bubble_sort() -> None:
    """
    Tests the insertion sort function with a sample list.
    
    :return: None
    """
    sample_list = [5, 2, 9, 1, 5, 6]
    bubbleSort(sample_list)
    assert sample_list == [1, 2, 5, 5, 6, 9], "bubble sort failed"
    print("Bubble sort passed!!")
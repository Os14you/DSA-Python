def insertionSort(lst: list) -> None:
    """
    Sorts a list using the insertion sort algorithm.
    
    :param list: A list of elements to be sorted.
    :return: A new list containing the sorted elements.
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
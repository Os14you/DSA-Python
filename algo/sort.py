def insertionSort(lst: list) -> None:
    """
    Sorts a list using the insertion sort algorithm.
    
    :param list: A list of elements to be sorted.

    Notes:
        The time complexity of this algorithm is O(N^2) in the average and
        worst cases and O(N) in the best case when the list is already sorted.
    """
    for i in range(len(lst)):
        element, j = lst[i], i - 1

        while j >= 0 and lst[j] > element:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = element

def bubbleSort(lst: list) -> None:
    """
    Sorts a list using the bubble sort algorithm.
    
    :param list: A list of elements to be sorted.

    Notes:
        The time complexity of this algorithm is O(N^2) in the average and
        worst cases and O(N) in the best case when the list is already sorted.
    """
    for amount_shifts in range(len(lst)):
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                swapped = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if not swapped:
            break

def selectionSort(lst: list) -> None:
    """
    Sorts a list using the selection sort algorithm.
    
    :param list: A list of elements to be sorted.

    Notes:
        The time complexity of this algorithm is O(N^2) in the average,
        worst and best cases.
    """
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        
        (lst[i], lst[min_idx]) = (lst[min_idx], lst[i])
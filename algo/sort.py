from typing import List, Any

def insertionSort(lst: List[Any]) -> None:
    """
    Sorts a list in-place using the insertion sort algorithm.

    Args:
        lst (List[Any]): A list of elements to be sorted.

    Notes:
        The time complexity is O(N^2) for average/worst cases and O(N)
        for the best case (already sorted list).
    """
    for i in range(1, len(lst)):
        element, j = lst[i], i - 1

        while j >= 0 and lst[j] > element:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = element

def bubbleSort(lst: List[Any]) -> None:
    """
    Sorts a list in-place using the bubble sort algorithm.

    Args:
        lst (List[Any]): A list of elements to be sorted.

    Notes:
        The time complexity is O(N^2) for average/worst cases and O(N)
        for the best case (already sorted list) due to the swap check.
    """
    for amount_shifts in range(len(lst)):
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                swapped = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if not swapped:
            break

def selectionSort(lst: List[Any]) -> None:
    """
    Sorts a list in-place using the selection sort algorithm.

    Args:
        lst (List[Any]): A list of elements to be sorted.

    Notes:
        The time complexity is O(N^2) in all cases (average, worst, and best)
        because it always performs the same number of comparisons.
    """
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        
        (lst[i], lst[min_idx]) = (lst[min_idx], lst[i])
    
def mergeSort(lst: List[Any]) -> List[Any]:
    """
    Sorts a list using the merge sort algorithm. This is not an in-place sort.

    Args:
        lst (List[Any]): A list of elements to be sorted.

    Returns:
        List[Any]: A new list containing the sorted elements.

    Notes:
        The time complexity is O(N * log(N)) in all cases.
        The space complexity is O(N) due to the need for temporary lists.
    """

    if len(lst) < 2:
        return lst[:]
    
    middle = len(lst) // 2
    left  = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])

    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    
    while i < len(left):
        merged.append(left[i])
        i+=1
    
    while j < len(right):
        merged.append(right[j])
        j+=1
    
    return merged

def quickSort(lst: List[Any], start: int, end: int) -> None:
    """
    Sorts a portion of a list in-place using the quick sort algorithm.

    Args:
        lst (List[Any]): The list of elements to be sorted.
        start (int): The starting index of the portion to sort.
        end (int): The ending index of the portion to sort.

    Notes:
        The time complexity is O(N * log(N)) on average and O(N^2) in the
        worst case (e.g., an already sorted list with a bad pivot choice).
    """

    def partition(lst: List[Any], low: int, high: int) -> int:
        """
        Partitions the list using the Lomuto partition scheme.
        
        It rearranges elements such that elements smaller than the pivot
        are on its left, and elements greater are on its right.

        Args:
            sub_lst (List[Any]): The list being partitioned.
            low (int): The starting index of the partition.
            high (int): The ending index (and pivot element index).

        Returns:
            int: The final index of the pivot element.
        """
        pivot = lst[high]
        pivotIdx = low - 1

        for i in range(low, high):
            if lst[i] <= pivot:
                pivotIdx+=1
                lst[i], lst[pivotIdx] = lst[pivotIdx], lst[i]
        
        lst[pivotIdx], lst[high] = lst[high], lst[pivotIdx]
        return pivotIdx

    if start >= end:
        return
    
    pivot = partition(lst, start, end)
    quickSort(lst, start, pivot-1)
    quickSort(lst, pivot+1, end)

def countSort(lst: List[Any], MAX_NUM: int) -> None:
    """
    Sorts a list of non-negative integers in-place using the counting sort algorithm.

    This algorithm is efficient when the range of input data (k) is not
    significantly larger than the number of elements (N).

    Args:
        lst (List[int]): A list of non-negative integers to be sorted.
        max_value (int): The maximum possible value in the list.

    Raises:
        ValueError: If the list contains negative numbers.

    Notes:
        - Time Complexity: O(N + k), where N is the number of elements
          and k is the `max_value`.
        - Space Complexity: O(k) to store the count of elements.
    """
    if not all(isinstance(x, int) and x >= 0 for x in lst):
        raise ValueError("All elements in the list must be non-negative integers.")
    
    count = [0] * (MAX_NUM+1)

    for i in lst:
        count[i] += 1

    j = 0
    for i in range(len(count)):
        repeats = count[i]
        while repeats > 0:
            lst[j] = i
            j+=1
            repeats -= 1
            
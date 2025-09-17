from algo.sort import (
    insertionSort,
    bubbleSort,
    selectionSort,
    mergeSort,
    quickSort,
    countSort
)

def test_all_sorting_functions():
    """
    Tests all sorting functions with a variety of test cases and prints the results.
    """
    print("🚀 Starting tests for all sorting algorithms...\n")

    # A dictionary mapping function names to the actual function objects
    sorters = {
        "insertionSort": insertionSort,
        "bubbleSort": bubbleSort,
        "selectionSort": selectionSort,
        "mergeSort": mergeSort,
        "quickSort": quickSort,
        "countSort": countSort,
    }

    # A dictionary of test cases to cover different scenarios
    test_cases = {
        "Random List": [5, 1, 4, 2, 8, 9, 3],
        "Empty List": [],
        "Single Element": [42],
        "Already Sorted": [10, 20, 30, 40, 50],
        "Reverse Sorted": [50, 40, 30, 20, 10],
        "With Duplicates": [4, 2, 7, 2, 7, 4, 4],
        "With Negatives": [-5, 2, -8, 1, 0, -4],
    }

    # Loop through each sorting function and test it with each case
    for func_name, sort_function in sorters.items():
        print(f"--- Testing: {func_name} ---")
        success_count = 0
        for case_name, original_list in test_cases.items():
            
            # --- PREPARATION ---
            # Create a copy, as most functions sort in-place!
            list_copy = original_list.copy()
            
            # The universally correct answer is given by Python's built-in sorted()
            expected_result = sorted(original_list)
            
            # Special handling for countSort, which only accepts non-negative integers
            if func_name == "countSort" and any(x < 0 for x in list_copy):
                print(f"  ⚪ SKIPPING: '{case_name}' (contains negative numbers).")
                continue

            # --- EXECUTION ---
            try:
                if func_name == "mergeSort":
                    # mergeSort is not in-place; it returns the sorted list
                    actual_result = sort_function(list_copy)
                else:
                    # All other functions sort in-place
                    if func_name == "quickSort":
                        if list_copy: # Avoid index errors on empty lists
                            sort_function(list_copy, 0, len(list_copy) - 1)
                    elif func_name == "countSort":
                         if list_copy: # Find max value for the function argument
                            max_val = max(list_copy)
                            sort_function(list_copy, max_val)
                    else:
                        sort_function(list_copy)
                    
                    actual_result = list_copy

                # --- VERIFICATION ---
                if actual_result == expected_result:
                    print(f"  ✅ PASS: '{case_name}'")
                    success_count += 1
                else:
                    print(f"  ❌ FAIL: '{case_name}'")
                    print(f"     Expected: {expected_result}")
                    print(f"     Got:      {actual_result}")
            
            except Exception as e:
                print(f"  💥 ERROR: '{case_name}' raised an exception: {e}")

        print("-" * (len(func_name) + 14) + "\n")

# To run the tests when you execute the file:
if __name__ == "__main__":
    test_all_sorting_functions()
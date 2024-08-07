from random import randint
from time import process_time

# Quick sort
def quick_sort(input):

    if len(input) < 2:
        return input

    left, center, right = [], [], []

    pivot = input[randint(0, len(input) - 1)]

    for val in input:

        if val < pivot:
            left.append(val)

        elif val == pivot:
            center.append(val)

        elif val > pivot:
            right.append(val)

    return quick_sort(left) + center + quick_sort(right)

# Base merge 
def base_merge(left, right):

    if len(left) < 1:
        return right
    
    if len(right) < 1:
        return left
    
    merged = []
    left_ind = right_ind = 0

    while len(merged) < (len(left) + len(right)):

        left_val = left[left_ind]
        right_val = right[right_ind]

        if left_val <= right_val:
            merged.append(left_val)
            left_ind += 1
        else:
            merged.append(right_val)
            right_ind += 1

        if left_ind == len(left):
            merged += right[right_ind:]
            break

        if right_ind == len(right):
            merged += left[left_ind:]
            break

    return merged

# Merge sort
def merge_sort(input):
    
    if len(input) < 2:
        return input
    
    pivot = len(input) // 2

    return base_merge(merge_sort(input[:pivot]), merge_sort(input[pivot:]))

# Helper
def measure_speed(func, array):

    t_start = process_time()
    func(array)
    t_finish = process_time()

    return t_finish-t_start

ARRAY_SMALL = 20000
ARRAY_MEDIUM = 50000
ARRAY_LARGE = 100000

# Main
def main():

    print("-- Quick sort showcase:")
    array_tiny = [randint(0, 200) for i in range(15)]
    print("Unsorted array:", array_tiny)
    print("Sorted array:", quick_sort(array_tiny), "\n\n")
    
    array_small = [randint(0, 900) for i in range(ARRAY_SMALL)]
    array_small_sorted = list(range(ARRAY_SMALL))

    array_medium = [randint(0, 900) for i in range(ARRAY_MEDIUM)]
    array_medium_sorted = list(range(ARRAY_MEDIUM))

    array_large = [randint(0, 900) for i in range(ARRAY_LARGE)]
    array_large_sorted = list(range(ARRAY_LARGE))

    print("-- Sorting speed comparison:\n")

    # Small arrays
    print("-- Small array:")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_small))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_small))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_small))
    print("-- Small array (sorted):")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_small_sorted))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_small_sorted))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_small_sorted), "\n")
   
    # Medium arrays
    print("-- Medium array:")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_medium))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_medium))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_medium))
    print("-- Medium array (sorted):")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_medium_sorted))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_medium_sorted))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_medium_sorted), "\n")

    # Large arrays
    print("-- Large array:")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_large))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_large))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_large))
    print("-- Large array (sorted):")
    print("Quick sort: elapsed time in seconds:", measure_speed(quick_sort, array_large_sorted))
    print("Merge sort: elapsed time in seconds:", measure_speed(merge_sort, array_large_sorted))
    print("Default sort: elapsed time in seconds:", measure_speed(sorted, array_large_sorted), "\n")

if __name__ == "__main__":
    main()


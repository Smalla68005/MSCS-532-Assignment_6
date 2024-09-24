import random
import timeit
import numpy as np

# Deterministic Median of Medians 
def median_of_medians(arr, k):
    # Divide array into sublists of 5 elements each
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    #Find median of medians recursively
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioin the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)

    # Determine the kth element
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Randomized Quickselect 
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)
    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

# Function to time the algorithms using timeit
def time_algorithm(algorithm, arr, k):
    # Measure execution time for one call
    timer = timeit.Timer(lambda: algorithm(arr.copy(), k))
    n_runs = 10
    time_taken = timer.timeit(number=n_runs) / n_runs
    return time_taken

# Helper to measure both algorithms on given input
def measure_algorithms(arr, k):

    # Time deterministic algorithm
    det_time = time_algorithm(lambda x, y: median_of_medians(x, y), arr, k)

    # Time randomized algorithm
    rand_time = time_algorithm(lambda x, y: randomized_select(x, 0, len(x)-1, y), arr, k)

    return det_time, rand_time

# Testing with different array sizes and distributions
input_sizes = [100, 1000, 5000, 10000]
distributions = {
    'random': lambda n: np.random.randint(0, 10000, n),
    'sorted': lambda n: np.arange(n),
    'reverse_sorted': lambda n: np.arange(n, 0, -1)
}

# Analysis for different input sizes and distributions
results = {}
for dist_name, dist_func in distributions.items():
    results[dist_name] = []
    print(f"Distribution: {dist_name}")
    for size in input_sizes:
        arr = dist_func(size)
        k = len(arr) // 2  # Looking for the median element
        det_time, rand_time = measure_algorithms(arr, k)
        print(f"Size: {size}, Det Time: {det_time:.6f}s, Rand Time: {rand_time:.6f}s")
        results[dist_name].append((size, det_time, rand_time))

import timeit
import matplotlib.pyplot as plt
import random
import good_sorts
import bad_sorts
import sys

sys.setrecursionlimit(200000)

def run_experiment():
    # Experiment Setup
    list_lengths = list(range(0, 1001, 50))
    num_runs = 10
    
    print(f"Starting Experiment 4: Quick vs Merge vs Heap")
    print(f"List Sizes: {list_lengths}")
    print(f"Runs per size: {num_runs}")
    
    times_quick = []
    times_merge = []
    times_heap = []
    
    for length in list_lengths:
        print(f"Testing list length: {length}")
        
        # Quick Sort
        time_q = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.quicksort(L)
            end = timeit.default_timer()
            time_q += (end - start)
        times_quick.append(time_q / num_runs)
        
        # Merge Sort
        time_m = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.mergesort(L)
            end = timeit.default_timer()
            time_m += (end - start)
        times_merge.append(time_m / num_runs)
        
        # Heap Sort
        time_h = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.heapsort(L)
            end = timeit.default_timer()
            time_h += (end - start)
        times_heap.append(time_h / num_runs)
        
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, times_quick, label='Quick Sort', marker='o')
    plt.plot(list_lengths, times_merge, label='Merge Sort', marker='s')
    plt.plot(list_lengths, times_heap, label='Heap Sort', marker='^')
    
    plt.title('Figure 5: Runtime Comparison of Good Sorts')
    plt.xlabel('List Length')
    plt.ylabel('Average Time (s)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment4_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

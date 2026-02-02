import timeit
import matplotlib.pyplot as plt
import good_sorts
import bad_sorts
import sys
import math

sys.setrecursionlimit(5000)

def run_experiment():
    # Experiment Setup
    length = 2500
    runs = 10
    max_swaps = int(length * math.log(length) / 2)
    swap_counts = [0, 10, 50, 100, 200, 400, 800, 1600, 3200, max_swaps]
    
    times_quick = []
    times_merge = []
    times_heap = []
    
    print(f"Starting Experiment 5: Quick Sort Worst Case Analysis")
    print(f"Fixed List Length: {length}")
    print(f"Swap counts to test: {swap_counts}")
    
    for swaps in swap_counts:
        print(f"Testing swaps: {swaps}")
        
        # Quick Sort
        t_q = 0
        for _ in range(runs):
            L = bad_sorts.create_near_sorted_list(length, length, swaps)
            start = timeit.default_timer()
            good_sorts.quicksort(L)
            t_q += (timeit.default_timer() - start)
        times_quick.append(t_q / runs)
        
        # Merge Sort
        t_m = 0
        for _ in range(runs):
            L = bad_sorts.create_near_sorted_list(length, length, swaps)
            start = timeit.default_timer()
            good_sorts.mergesort(L)
            t_m += (timeit.default_timer() - start)
        times_merge.append(t_m / runs)
        
        # Heap Sort
        t_h = 0
        for _ in range(runs):
            L = bad_sorts.create_near_sorted_list(length, length, swaps)
            start = timeit.default_timer()
            good_sorts.heapsort(L)
            t_h += (timeit.default_timer() - start)
        times_heap.append(t_h / runs)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(swap_counts, times_quick, label='Quick Sort', marker='o')
    plt.plot(swap_counts, times_merge, label='Merge Sort', marker='s')
    plt.plot(swap_counts, times_heap, label='Heap Sort', marker='^')
    
    plt.title(f'Figure 6: Effect of Sortedness on Good Sorts (Length {length})')
    plt.xlabel('Number of Swaps (0 = Sorted)')
    plt.ylabel('Average Time (s)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment5_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

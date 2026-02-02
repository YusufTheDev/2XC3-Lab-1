import timeit
import matplotlib.pyplot as plt
import good_sorts
import bad_sorts
import sys

def run_experiment():
    list_lengths = list(range(0, 101, 5))
    num_runs = 50
    
    print(f"Starting Experiment 8: Small List Comparison (Insertion vs Good Sorts)")
    print(f"List Sizes: {list_lengths}")
    
    times_insertion = []
    times_quick = []
    times_merge = []
    
    for length in list_lengths:
        # Insertion Sort
        t_i = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, 1000)
            start = timeit.default_timer()
            bad_sorts.insertion_sort(L)
            t_i += (timeit.default_timer() - start)
        times_insertion.append(t_i / num_runs)
        
        # Quick Sort
        t_q = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, 1000)
            start = timeit.default_timer()
            good_sorts.quicksort(L)
            t_q += (timeit.default_timer() - start)
        times_quick.append(t_q / num_runs)
        
        # Merge Sort
        t_m = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, 1000)
            start = timeit.default_timer()
            good_sorts.mergesort(L)
            t_m += (timeit.default_timer() - start)
        times_merge.append(t_m / num_runs)
        
    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, times_insertion, label='Insertion Sort', marker='^')
    plt.plot(list_lengths, times_quick, label='Quick Sort', marker='o')
    plt.plot(list_lengths, times_merge, label='Merge Sort', marker='s')
    
    plt.title('Figure 9: Insertion Sort vs Good Sorts (Small Lists)')
    plt.xlabel('List Length')
    plt.ylabel('Average Time (s)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment8_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

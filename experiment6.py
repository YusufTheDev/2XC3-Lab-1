import timeit
import matplotlib.pyplot as plt
import good_sorts
import bad_sorts
import sys

sys.setrecursionlimit(200000)

def run_experiment():
    list_lengths = [10, 100, 1000, 5000, 10000, 20000, 50000]
    num_runs = 10
    
    print(f"Starting Experiment 6: Quick Sort vs Dual Pivot Quick Sort")
    print(f"List Sizes: {list_lengths}")
    
    times_quick = []
    times_dual = []
    
    for length in list_lengths:
        print(f"Testing list length: {length}")
        
        # Quick Sort
        t_q = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.quicksort(L)
            t_q += (timeit.default_timer() - start)
        times_quick.append(t_q / num_runs)
        
        # Dual Pivot Quick Sort
        t_dq = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.dual_quicksort(L)
            t_dq += (timeit.default_timer() - start)
        times_dual.append(t_dq / num_runs)
        
    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, times_quick, label='Quick Sort (1 Pivot)', marker='o')
    plt.plot(list_lengths, times_dual, label='Dual Quick Sort (2 Pivots)', marker='s')
    
    plt.title('Figure 7: Quick Sort vs Dual Pivot Quick Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Time (s)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment6_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

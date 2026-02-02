import timeit
import matplotlib.pyplot as plt
import good_sorts
import bad_sorts
import sys

sys.setrecursionlimit(200000)

def run_experiment():
    list_lengths = [10, 100, 1000, 5000, 10000, 20000, 50000]
    num_runs = 10
    
    print(f"Starting Experiment 7: Merge Sort vs Bottom-Up Merge Sort")
    print(f"List Sizes: {list_lengths}")
    
    times_merge = []
    times_bottom_up = []
    
    for length in list_lengths:
        print(f"Testing list length: {length}")
        
        # Recursive Merge Sort
        t_m = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.mergesort(L)
            t_m += (timeit.default_timer() - start)
        times_merge.append(t_m / num_runs)
        
        # Bottom-Up Merge Sort
        t_bum = 0
        for _ in range(num_runs):
            L = bad_sorts.create_random_list(length, length)
            start = timeit.default_timer()
            good_sorts.bottom_up_mergesort(L)
            t_bum += (timeit.default_timer() - start)
        times_bottom_up.append(t_bum / num_runs)
        
    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, times_merge, label='Recursive Merge Sort', marker='o')
    plt.plot(list_lengths, times_bottom_up, label='Bottom-Up Merge Sort', marker='s')
    
    plt.title('Figure 8: Recursive vs Bottom-Up Merge Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Time (s)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment7_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

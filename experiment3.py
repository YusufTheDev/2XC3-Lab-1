import timeit
import matplotlib.pyplot as plt
from bad_sorts import bubble_sort, selection_sort, insertion_sort, create_near_sorted_list

def run_experiment3():
    list_len = 1000
    runs = 10
    max_val = 1000
    swaps_counts = list(range(0, 501, 25)) # 0 to 500 swaps? Or more?
    # 500 swaps on 1000 elements is somewhat randomized.
    # Let's go up to 1000 swaps.
    swaps_counts = list(range(0, 1001, 50))
    
    b_times = []
    s_times = []
    i_times = []
    
    print("Starting Experiment 3: Near-Sorted Analysis")
    
    for swaps in swaps_counts:
        print(f"Testing swaps: {swaps}")
        
        # Bubble
        t = 0
        for _ in range(runs):
            L = create_near_sorted_list(list_len, max_val, swaps)
            start = timeit.default_timer()
            bubble_sort(L)
            t += timeit.default_timer() - start
        b_times.append(t/runs)
        
        # Selection
        t = 0
        for _ in range(runs):
            L = create_near_sorted_list(list_len, max_val, swaps)
            start = timeit.default_timer()
            selection_sort(L)
            t += timeit.default_timer() - start
        s_times.append(t/runs)
        
        # Insertion
        t = 0
        for _ in range(runs):
            L = create_near_sorted_list(list_len, max_val, swaps)
            start = timeit.default_timer()
            insertion_sort(L)
            t += timeit.default_timer() - start
        i_times.append(t/runs)
        
    plt.figure(figsize=(10, 6))
    plt.plot(swaps_counts, b_times, label='Bubble Sort', marker='o')
    plt.plot(swaps_counts, s_times, label='Selection Sort', marker='s')
    plt.plot(swaps_counts, i_times, label='Insertion Sort', marker='^')
    
    plt.title(f'Experiment 3: Runtime vs Sortedness (Length={list_len})')
    plt.xlabel('Number of Swaps')
    plt.ylabel('Average Runtime (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('experiment3_results.png')
    print("Saved experiment3_results.png")

if __name__ == "__main__":
    run_experiment3()

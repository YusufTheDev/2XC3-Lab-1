import timeit
import matplotlib.pyplot as plt
import random
from bad_sorts import bubble_sort, selection_sort, insertion_sort, create_random_list

def run_experiment():
    # Experiment Setup
    list_sizes = list(range(0, 1001, 50))  # 0 to 1000, step 50
    runs_per_size = 10
    max_val = 1000

    print(f"Starting Experiment 1: Bubble vs Selection vs Insertion")
    print(f"List Sizes: {list_sizes}")
    print(f"Runs per size: {runs_per_size}")

    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in list_sizes:
        print(f"Testing list size: {size}")
        
        # Bubble Sort
        total_time = 0
        for _ in range(runs_per_size):
            L = create_random_list(size, max_val)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            total_time += (end - start)
        bubble_times.append(total_time / runs_per_size)

        # Selection Sort
        total_time = 0
        for _ in range(runs_per_size):
            L = create_random_list(size, max_val)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            total_time += (end - start)
        selection_times.append(total_time / runs_per_size)

        # Insertion Sort
        total_time = 0
        for _ in range(runs_per_size):
            L = create_random_list(size, max_val)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            total_time += (end - start)
        insertion_times.append(total_time / runs_per_size)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(list_sizes, selection_times, label='Selection Sort', marker='s')
    plt.plot(list_sizes, insertion_times, label='Insertion Sort', marker='^')
    
    plt.title('Experiment 1: Runtime Comparison of "Bad" Sorts')
    plt.xlabel('List Length')
    plt.ylabel('Average Runtime (seconds)')
    plt.legend()
    plt.grid(True)
    
    output_filename = 'experiment1_results.png'
    plt.savefig(output_filename)
    print(f"Graph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()

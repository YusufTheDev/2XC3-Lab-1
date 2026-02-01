import timeit
import matplotlib.pyplot as plt
from bad_sorts import bubble_sort, bubble_sort2, selection_sort, selection_sort2, create_random_list

def run_experiment2():
    sizes = list(range(0, 1001, 50))
    runs = 10
    max_val = 1000

    print("Starting Experiment 2...")

    # Data containers
    b_times = []
    b2_times = []
    s_times = []
    s2_times = []

    for size in sizes:
        print(f"Testing list size: {size}")
        
        # Bubble Sort vs Bubble Sort 2
        t_b = 0
        t_b2 = 0
        for _ in range(runs):
            L = create_random_list(size, max_val)
            L2 = L.copy()
            
            start = timeit.default_timer()
            bubble_sort(L)
            t_b += timeit.default_timer() - start
            
            start = timeit.default_timer()
            bubble_sort2(L2)
            t_b2 += timeit.default_timer() - start
            
        b_times.append(t_b / runs)
        b2_times.append(t_b2 / runs)
        
        # Selection Sort vs Selection Sort 2
        t_s = 0
        t_s2 = 0
        for _ in range(runs):
            L = create_random_list(size, max_val)
            L2 = L.copy()
            
            start = timeit.default_timer()
            selection_sort(L)
            t_s += timeit.default_timer() - start
            
            start = timeit.default_timer()
            selection_sort2(L2)
            t_s2 += timeit.default_timer() - start
            
        s_times.append(t_s / runs)
        s2_times.append(t_s2 / runs)

    # Plot Bubble Sort Comparison
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, b_times, label='Bubble Sort', marker='o')
    plt.plot(sizes, b2_times, label='Bubble Sort 2', marker='s')
    plt.title('Experiment 2: Bubble Sort vs Optimized Bubble Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Runtime (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('experiment2_bubble.png')
    print("Saved experiment2_bubble.png")

    # Plot Selection Sort Comparison
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, s_times, label='Selection Sort', marker='o')
    plt.plot(sizes, s2_times, label='Selection Sort 2', marker='s')
    plt.title('Experiment 2: Selection Sort vs Optimized Selection Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Runtime (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('experiment2_selection.png')
    print("Saved experiment2_selection.png")

if __name__ == "__main__":
    run_experiment2()

import matplotlib.pyplot as plt
import random
import time

def big_O():
    n_inputs = []
    time_taken = []
    for i in range(1000):
        n_inputs.append(i)
        start_time  = time.time()
        arr = random.sample(range(0,1001), i)
        bubble_sort(arr)
        end_time = time.time()
        t = end_time - start_time
        time_taken.append(t)
        print(i, t)

    plt.plot(n_inputs, time_taken)
    plt.title("Bubble sort performance")
    plt.xlabel("Number of inputs")
    plt.ylabel("Time")
    plt.show()


def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True 

def bubble_sort(arr):
    while not isSorted(arr):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j -1], arr[j] = arr[j], arr[j - 1] # swap items

    return arr

def main():
    arr = random.sample(range(0,101), 10)
    print(f"Original array: {arr}")
    sorted_arr = bubble_sort(arr)    
    print(f"Sorted array: {sorted_arr}")

    big_O()

if __name__ == "__main__":
    main()
import numpy as np
import time
import matplotlib.pyplot as plt

def merge_sort(arr):

    if len(arr) == 1:
        return arr
    
    else:
        mid = int(len(arr) // 2)
        first = merge_sort(arr[:mid])
        last = merge_sort(arr[mid:])

        sortedArr = []

        i = j = k = 0

        while i < len(first) and j < len(last):
            if first[i] < last[j]:
                sortedArr.append(first[i])
                i += 1
            else:
                sortedArr.append(last[j])
                j += 1

        while i < len(first):
            sortedArr.append(first[i])
            i += 1

        while j < len(last):
            sortedArr.append(last[j])
            j += 1

        return sortedArr

def show_graph(x, y):
    plt.plot(x, y)
    plt.title("Insertion sort Performance")
    plt.xlabel("Number of inputs")
    plt.ylabel("Time (s)")
    plt.show()

if __name__ == "__main__":
    numOfInputs = []
    times = []

    for i in range(1, 10000):
        arr = np.random.randint(1, i * 10, i)
        start = time.time()
        sortedArr = merge_sort(arr)
        end = time.time()


        numOfInputs.append(len(sortedArr))
        times.append(end - start)

        print(len(numOfInputs), end - start)
        
    show_graph(numOfInputs, times)
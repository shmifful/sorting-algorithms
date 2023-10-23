import numpy as np
import matplotlib.pyplot as plt
import time

def sortArr(arr, i):
    for j in range(0, i):
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

    return arr

def insertion_sort(arr):
    sortedArr = arr
    for i in range(1, len(arr)):
        if sortedArr[i] < sortedArr[i - 1]:
            sortedArr = sortArr(arr, i)

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

    for i in range(2500):
        arr = np.random.randint(0, i * 10, i)
        start = time.time()
        insertion_sort(arr)
        end = time.time()

        numOfInputs.append(len(arr))
        times.append(end - start)

        print(len(numOfInputs), end - start, "\n")
        
    show_graph(numOfInputs, times)
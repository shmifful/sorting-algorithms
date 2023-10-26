import numpy as np
import matplotlib.pyplot as plt
import time

def selection_sort(arr):
    for i in range(len(arr) - 1):
        elMin = i
        for j in range(i, len(arr)):
            if arr[j] < arr[elMin]:
                elMin = j

        if elMin != i:
            arr[i], arr[elMin] = arr[elMin], arr[i]

    return arr

def show_graph(x, y):
    plt.plot(x, y)
    plt.title("Selection sort Performance")
    plt.xlabel("Number of inputs")
    plt.ylabel("Time (s)")
    plt.show()

if __name__ == "__main__":
    numOfInputs = []
    times = []

    for i in range(2500):
        arr = np.random.randint(0, i * 10, i)
        start = time.time()
        selection_sort(arr)
        end = time.time()

        numOfInputs.append(len(arr))
        times.append(end - start)

        print(len(numOfInputs), end - start, "\n")
        
    show_graph(numOfInputs, times)
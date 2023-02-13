import json
import random
import time
import matplotlib.pyplot as plt
import threading
threading.stack_size(33554432)
import sys
sys.setrecursionlimit(20000)

# Load the JSON file
with open("ex2.json", "r") as file:
    data = json.load(file)

# Randomize the elements in the inner lists
for i in range(len(data)):
    random.shuffle(data[i])

# Write the randomized data back to the JSON file
with open("ex2.5.json", "w") as file:
    json.dump(data, file)

def func1(arr, low, high):
    while low < high:
        pi = func2(arr, low, high)
        if pi - low < high - pi:
            func1(arr, low, pi-1)
            low = pi + 1
        else:
            func1(arr, pi + 1, high)
            high = pi - 1

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Load the JSON data from the links
with open("ex2.5.json") as f:
    data = json.load(f)

# Initialize the arrays to store the sorting times
input_sizes = []
sorting_times = []

# Sort each input and measure the time taken
for i, input_array in enumerate(data):
    n = len(input_array)
    input_sizes.append(n)
    start_time = time.time()
    func1(input_array, 0, n-1)
    end_time = time.time()
    sorting_times.append(end_time - start_time)

# Plot the results
plt.plot(input_sizes, sorting_times, 'o-')
plt.xlabel("Input Size")
plt.ylabel("Sorting Time (s)")
plt.title("Quick Sort Timing Results")
plt.show()
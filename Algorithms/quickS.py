import random
import time

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def randpartition(arr, low, high):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)

# The QuickSort function implementation
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if (low < high):

        pi = randpartition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

# Function to print an array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)

# record start time
start = time.time()

# define a sample code segment
a = 0
for i in range(1000):
	a += (i**100)

# record end time
end = time.time()

# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :", (end-start) * 10**3, "ms")

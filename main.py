import time, sys, random

def insertionSort(arr):
    # Traverse through the entire array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared and inserted
        j = i - 1  # Start with the previous element

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position in the sorted part of the array
        arr[j + 1] = key


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        mergeSort(left_half)  # Recursively sort the first half
        mergeSort(right_half)  # Recursively sort the second half

        i = j = k = 0

        # Merge the two halves back together
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in both halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def hybridSort(arr):
    if len(arr) <= 5:
        return insertionSort(arr)
    else:
        return mergeSort(arr)


def randomLists(len, rangeStart, rangeEnd):
    return [random.randint(rangeStart, rangeEnd) for i in range(len)]

numTests = 10
listLen = 1000

for i in range(numTests):
    ranLists = randomLists(listLen, 1, 10000)

insertStart = time.time()
insertionSort(ranLists.copy())
insertEnd = time.time()
insertion = insertionSort.__code__
insertionSize = sys.getsizeof(insertion)
print("Insertion sort:")
print("------------")
print("Time taken to happen: ", insertEnd - insertStart)
print("Memory size of Insertion Sort ", insertionSize)


mergeStart = time.time()
mergeSort(ranLists.copy())
mergeEnd = time.time()
merge = mergeSort.__code__
mergeSize = sys.getsizeof(merge)
print("\nMerge sort:")
print("------------")
print("Time taken to happen: ", mergeEnd - mergeStart)
print("Memory size of Merge Sort ", mergeSize)


hybridStart = time.time()
hybridSort(ranLists.copy())
hybrideEnd = time.time()
hybrid = hybridSort.__code__
hybridSize = sys.getsizeof(hybrid)
print("\nHybrid test: ")
print("------------")
print("Time taken to happen: ", hybrideEnd - hybridStart)
print("Memory size of Merge Sort ", hybridSize)

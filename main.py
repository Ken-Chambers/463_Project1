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
    if len(arr) <= 16:
        return insertionSort(arr)
    else:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        mergeSort(left_half)  
        mergeSort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        if len(arr) <= 16:
            insertionSort(arr)


def randomLists(len, rangeStart, rangeEnd):
    return [random.randint(rangeStart, rangeEnd) for i in range(len)]

numTests = 10
listLen = 500

for i in range(numTests):
    ranLists = randomLists(listLen, 1, 10000)


insertStart100 = time.time()
insertionSort(ranLists.copy())
insertEnd100 = time.time()
insertion100 = insertionSort.__code__
insertionSize100 = sys.getsizeof(insertion100)
print("\nInsertion sort with 500 items:")
print("------------")
print("Time taken to happen: ", insertEnd100 - insertStart100, "seconds.")
print("Memory size of Insertion Sort ", insertionSize100)


mergeStart = time.time()
mergeSort(ranLists.copy())
mergeEnd = time.time()
merge = mergeSort.__code__
mergeSize = sys.getsizeof(merge)
print("\nMerge sort with 500 items:")
print("------------")
print("Time taken to happen: ", mergeEnd - mergeStart, "seconds.")
print("Memory size of Merge Sort ", mergeSize)


hybridStart = time.time()
hybridSort(ranLists.copy())
hybridEnd = time.time()
hybrid = hybridSort.__code__
hybridSize = sys.getsizeof(hybrid)
print("\nHybrid test with 500 items: ")
print("------------")
print("Time taken to happen: ", hybridEnd - hybridStart, "seconds.")
print("Memory size of hybridSort ", hybridSize)

print("\n---------------------")

numTests1000 = 10
listLen = 1000

for i in range(numTests1000):
    ranLists1000 = randomLists(listLen, 1, 10000)

insertStart = time.time()
insertionSort(ranLists1000.copy())
insertEnd = time.time()
insertion = insertionSort.__code__
insertionSize = sys.getsizeof(insertion)
print("\nInsertion sort with 1000 items:")
print("------------")
print("Time taken to happen: ", insertEnd - insertStart, "seconds.")
print("Memory size of Insertion Sort ", insertionSize)


mergeStart = time.time()
mergeSort(ranLists1000.copy())
mergeEnd = time.time()
merge = mergeSort.__code__
mergeSize = sys.getsizeof(merge)
print("\nMerge sort with 1000 items:")
print("------------")
print("Time taken to happen: ", mergeEnd - mergeStart, "seconds.")
print("Memory size of Merge Sort ", mergeSize)


hybridStart = time.time()
hybridSort(ranLists1000.copy())
hybridEnd = time.time()
hybrid = hybridSort.__code__
hybridSize = sys.getsizeof(hybrid)
print("\nHybrid test with 1000 items: ")
print("------------")
print("Time taken to happen: ", hybridEnd - hybridStart, "seconds.")
print("Memory size of hybridSort ", hybridSize)

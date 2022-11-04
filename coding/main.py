
# Insertion sort in python

def inssertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # compare key with each element on the left of it until and element
        # small for descring order. change key<array[j] to key > array[j

        while j>= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the elemetn just smaller than it
        array[j + 1] = key


def bubbleSort(array):
    # loop for access each array element
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            #compare two djanecent elements
            # change > to < to sort in descending order
            if array[j] > array[j +1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

def selectionSort(array, size):

    for step in range(size):
        mid_idx = step

        for i in range(step + 1, size):
            if array[i] < array[mid_idx]:
                mid_idx = i
        (array[step], array[mid_idx]) = (array[mid_idx], array[step])

# Merge Sort in python

def mergeSort(array):
    if len(array) > 1:
        r = len(array) // 2
        L = array[:r]
        M = array[r:]
        # sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# quick sort in python
# function to find the partition

def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

        (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def LinearSearch(array, n , k):
    for j in range(0, n):
        if (array[j] == k):
            print('element found at index' , j )
            return True
    print("Element not found")
    return False



def ImprovedLinearSearch(array, element):
    size = len(array)
    for j in range(0 , size):
        if array[j] == element:
            return True
    return False


def BinarySearch(array, k, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if k == array[mid]:
            return mid

        elif k > array[mid]:
            return BinarySearch(array, k, mid + 1, high)
        else:
            return BinarySearch(array, k, low, mid - 1)



real_raw_input = vars(__builtins__).get('raw_input',input)

key = real_raw_input("Data here : ")

data = [10,20,40,50, 30]
size = len(data)
# quicksort(data, 0, size - 1)
# print('Sorted Array in Ascending Order:')
print(ImprovedLinearSearch(data, real_raw_input))
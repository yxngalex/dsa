def heap_sort(array):  # O(n log n) on best, avg, worst
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        swap(array, 0, i)
        heapify(array, i, 0)

    return array


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is greater than root
    if left < n and array[left] > array[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and array[right] > array[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        swap(array, i, largest)
        heapify(array, n, largest)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    print("Original:", arr)
    sorted_arr = heap_sort(arr)
    print("Sorted:", sorted_arr)


if __name__ == '__main__':
    main()

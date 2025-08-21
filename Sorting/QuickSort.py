# Divide and conquer
def quick_sort(array, left, right):  # O(n log n) on avg
    if left < right:
        pivot = right
        partition_index = partition(array, pivot, left, right)

        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, right)
    return array


def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, partition_index)
            partition_index += 1

    swap(array, right, partition_index)
    return partition_index


def swap(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    print("Original:", arr)
    sorted_arr = quick_sort(arr, 0, len(arr) - 1)
    print("Sorted:", sorted_arr)


if __name__ == '__main__':
    main()

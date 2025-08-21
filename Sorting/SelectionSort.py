def selection_sort(array):  # O(n^2) on avg
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                # update the minimum
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    selection_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

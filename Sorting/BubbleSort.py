def bubble_sort(array):  # O(n^2) on avg
    length = len(array)
    for i in range(length):
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                # Swap numbers
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    bubble_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

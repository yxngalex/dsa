def insertion_sort(array):  # O(n^2) on avg
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    return array


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    insertion_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

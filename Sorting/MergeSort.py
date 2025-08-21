# Divide and conquer
def merge_sort(array):  # O(n log(n)) on avg
    if len(array) == 1:
        return array

    # Split array in into right and left
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
    print('left', left)
    print('right', right)

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]


def main():
    arr = [99, 44, 6, 2, 1, 5, 63, 78, 283, 4, 0]
    arr[:] = merge_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

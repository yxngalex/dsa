''' 
 Google Question
 Given an array return a first reoccuring character

 INPUT = [2, 5, 1, 2, 3, 5, 1, 2, 4]
 OUTPUT = 2

 INPUT = [2, 1, 1, 2, 3, 5, 1, 2, 4]
 OUTPUT = 1

 INPUT = [2, 3, 4, 6]
 OUTPUT = None
'''

def check(array):
    if not array:
        return None

    seen = set()
    for i in range(len(array)):
        if array[i] in seen:
            return array[i]
        else:
            seen.add(array[i])

    return None


def main():
    arr1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    arr2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    arr3 = [2, 3, 4, 6]
    print(check(arr1))
    print(check(arr2))
    print(check(arr3))


if __name__ == "__main__":
    main()

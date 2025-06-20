'''
Given two arrays that are sorted, merge them into a big one that is still sorted

Input:
arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]

Output:
[0, 3, 4, 6, 30, 31] (we have a duplicate 4, what should we do with it?)
'''

'''
    Solution: take both, sorted,
    for this solution I've decided to have duplicates.
    Go through each array get and element, and put it in a map as a key and count as a value
    Check the map with the second array and update the counter and the key
    In third array just go through elements and loop via the counter and just add in the third arr values and return it
'''

#O((n+m)log(n+m))
def mergeSortedArrays(arr1, arr2):
    mergedArr = []
    mergedMap = createMap(arr1, arr2)

    for elem in sorted(mergedMap.keys()):
        count = mergedMap[elem]
        for i in range(count):
            mergedArr.append(elem)

    return mergedArr


def createMap(arr1, arr2):
    elementsWithCounter = {} # map
    addArrayToMap(arr1, elementsWithCounter) #O(n)
    addArrayToMap(arr2, elementsWithCounter) #O(n)
    return elementsWithCounter



def addArrayToMap(arr, elementsMap):
    for i in range(len(arr)):
        if arr[i] in elementsMap:
            elementsMap[arr[i]] += 1 # current element goes up by 1
        else:
            elementsMap[arr[i]] = 1 # adds an element into the map 



# Two-pointer approach O(n + m)
def twoPointer(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1


    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


if __name__ == "__main__":
    print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))
    print(twoPointer([0, 3, 4, 31], [4, 6, 30]))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dir = {}
        for i, el in enumerate(nums):
            if el in dir:
                dir[el].append(i)
            else:
                dir[el] = [i]

        for el in nums:
            res = target - el
            if res == el and len(dir[res]) > 1:
                return dir[el]
            elif res != el and res in dir:
                return [dir[el][0], dir[res][0]]

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print("Indices:", result)

#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#输入: nums = [0,1,0,3,12]
#输出: [1,3,12,0,0]

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
            else:
                nums[i-count] = nums[i]

        n = len(nums)
        for j in range(count):
            nums[n-1-j] = 0




s = Solution()
l = [0,1,0,3,12]
print(l)
s.moveZeroes(l)
print(l)
'''
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

输入：nums = [2,2,1]
输出：1

输入：nums = [4,1,2,1,2]
输出：4


'''


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            x^=nums[i]

        return x


s = Solution()
l = [4,1,2,1,2]
print(s.singleNumber(l))
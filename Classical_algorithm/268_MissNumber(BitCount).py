'''
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

'''


from typing import List



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= nums[i]
            res ^= i
        res ^= n

        return res



s = Solution()
l = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(l))


'''
给你一个整数数组nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。

输入：nums = [1,2,1,3,2,5]
输出：[3,5]

'''


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor  = 0
        for i in range(len(nums)):
            xor ^=nums[i]
        print("First xor:",bin(xor))

        xor = xor&(-xor)
        print("Second xor:", bin(xor))

        res0 = 0
        res1 = 0
        for i, nums in enumerate(nums):
            if xor & nums == xor:
                res0 ^= nums
            else:
                res1 ^=nums
        res = []
        res.append(res0)
        res.append(res1)
        return res



s = Solution()
l = [1,2]

print(s.singleNumber(l))
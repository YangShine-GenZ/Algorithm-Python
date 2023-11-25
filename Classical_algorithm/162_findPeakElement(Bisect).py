'''
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
    或者返回索引 5， 其峰值元素为 6。


'''

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n-1
        print(r)
        while(l<=r):
            mid  = l+int((r-l)/2)
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return l








s = Solution()
l = [1,2,3,4,5,6,4,2,1,float('-inf')]
l2 = [1,3,2]
l1 = [1,float('-inf')]
print(s.findPeakElement(l1))

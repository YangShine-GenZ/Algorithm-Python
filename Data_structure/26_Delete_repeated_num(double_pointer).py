# 删除有序数组中的重复项
#给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

#输入：nums = [0,0,1,1,1,2,2,3,3,4]
#输出：5, nums = [0,1,2,3,4]
from typing import List



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #initialize
        slow = fast = 0
        # delete the repeated num
        # change the nums
        for fast in range(len(nums)):
            if(fast>0 and nums[fast-1]==nums[fast]):
                continue
            else:
                nums[slow] = nums[fast]
                slow+=1


        return slow

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)
#求三数之和是否为固定值


#输入：nums = [-1,0,1,2,-1,-4]
#输出：[[-1,-1,2],[-1,0,1]]

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        resList = []
        #sort the List
        nums.sort()


        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            first = nums[i]
            target = 0-first
            right = len(nums)-1
            #loop for b and c
            for left in range(i+1,len(nums)):
                if(nums[left]==nums[left-1] and left>i+1):
                    continue
                while(left<right and (nums[left]+nums[right])>target):
                    right-=1
                if(left==right):
                    break
                if(nums[left]+nums[right]==target):
                    resList.append([nums[i],nums[left],nums[right]])
        return resList

l = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(l))
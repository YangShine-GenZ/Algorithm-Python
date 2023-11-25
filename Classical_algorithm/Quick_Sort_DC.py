#快排


'''
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


'''

from typing import List


def Pivot(nums:List[int],l,r):
    if l>=r:
        return nums
    target = nums[l]
    left = l+1
    right = r
    while(left<right):
        while(left<right and nums[left]<=target):
            left+=1
        while(left<right and nums[right]>=target):
            right-=1
        if left==right:
            break
        nums[left],nums[right] = nums[right],nums[left]

    if nums[left]>target:
        nums[l],nums[left-1] = nums[left-1],nums[l]
        left-=1
    else:
        nums[l], nums[left] = nums[left], nums[l]
    Pivot(nums,l,left-1)
    Pivot(nums,left+1,r)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = nums
        Pivot(res,0,len(res)-1)
        return res




s = Solution()
l = [5,3,1,2,0,0]
print(s.sortArray(l))



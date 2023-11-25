'''
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


'''



from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            else:
                d[nums[i]]+=1
        return max(d.items(),key= lambda x:x[1])[0]





s = Solution()
l = [1, 2, 3, 2, 2, 2, 5, 4, 2]

print(s.majorityElement(l))
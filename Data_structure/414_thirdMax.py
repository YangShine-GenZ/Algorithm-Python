#给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

#输入：[3, 2, 1]
#输出：1
#解释：第三大的数是 1 。


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num0,num1,num2 = float('-inf'),float('-inf'),float('-inf')
        for i in range(len(nums)):
            if nums[i]>num0:
                num0,num1,num2 = nums[i],num0,num1
            elif num1<nums[i]<num0:
                num0,num1,num2 = num0,nums[i],num1
            elif num2<nums[i]<num1:
                num0,num1,num2 = num0,num1,nums[i]

        if num2 != float('-inf'):
            return num2
        else:
            return num0





s = Solution()
#l = [3,2,1,6,7,9,10]
l = [1,2,3]
print(s.thirdMax(l))
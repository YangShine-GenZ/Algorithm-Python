'''
找出当前排列的下一个排列
排列即 对于List [x,y,z]->int([xyz])
若不存在下一个排列，则返回最小排列

输入：nums = [1,2,3]
输出：[1,3,2]

输入：nums = [3,2,1]
输出：[1,2,3]

输入：nums = [1,1,5]
输出：[1,5,1]

'''

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i = n-1
        '''
        index = FindtheLast()
        swap(index,Lastmin())
        sorted(Lastmin:n) 
        '''
        if n == 0:
            return


        while(i>=0):
            if nums[i]<nums[i+1]:
                index = i
                break
            i-=1
            index = i
        if index == -1:
            left = index + 1
            right = n
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            print(nums)
            return
        #debug
        print(index)


        cur = nums[index+1]
        Lastmin = index+1
        for i in range(index+1,n+1):
            if nums[i]<=cur and nums[i]>nums[index]:
                cur = nums[i]
                Lastmin = i

        nums[index],nums[Lastmin] = nums[Lastmin],nums[index]
        #debug
        print(nums)

        left = index+1
        right = n
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
        # debug
        print(nums)


s = Solution()
l = [2,3,1,3,3]
print("List:",l)

#l = [2,2,4,3,1]
#l = [4,3,2,1]
s.nextPermutation(l)


'''
for i in range(30):
    s.nextPermutation(l)
'''




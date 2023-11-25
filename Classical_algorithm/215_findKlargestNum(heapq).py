import heapq
from typing import List

'''
找到第k大的数
输入: [3,2,1,5,6,4], k = 2
输出: 5

1.利用二叉堆，每次保存最大的k个数 时间复杂度 O(logk*n)

2.采用快排的思想

'''


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        eq = []
        for i in range(len(nums)):
            heapq.heappush(eq,nums[i])
            if len(eq)>k:
                heapq.heappop(eq)

        print(eq)
        return eq[0]




    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def Pivot(l, r):

            if l>=r:
                return nums[l]


            left = l + 1
            right = r


            target = nums[l]

            while left < right:
                while left < right and nums[left] <= target:
                    left += 1
                while right > left and nums[right] >= target:
                    right -= 1
                if left == right:
                    break
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] > target:
                nums[left - 1], nums[l] = nums[l], nums[left - 1]
                left -= 1
            else:
                nums[left], nums[l] = nums[l], nums[left]

            if left == n-k:
                return nums[left]

            if left < n-k:
                return Pivot(left+1,r)
            if left > n-k:
                return Pivot(l,left-1)

        res = Pivot(0, n - 1)


        print(nums)
        print("res:",res)

        return res



s = Solution()
l = [1,2,3,4]
s.findKthLargest(l,2)
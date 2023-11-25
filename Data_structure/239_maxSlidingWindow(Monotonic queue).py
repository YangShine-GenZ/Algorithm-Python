'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]

'''


from typing import List



class Monotonic_queue:

    def __init__(self):
        self.rlist = []

    def push(self, x: int):
        n = len(self.rlist)
        for i in range(n):
            if self.rlist[n-1-i] < x:
                self.rlist.pop(-1)
        self.rlist.append(x)




    def pop(self,x: int):
        if x == self.rlist[0]:
            self.rlist.pop(0)
        else:
            return

    def max(self):
        return self.rlist[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = Monotonic_queue()
        res = []
        for i in range(len(nums)):
            if i<k-1:
                mq.push(nums[i])
            else:
                mq.push(nums[i])
                res.append(mq.max())
                mq.pop(nums[i-k+1])

        return  res


s = Solution()
#l = [1,3,1,2,0,5]
l = [6,2,5,2,5,1,6]
k = 3
print(s.maxSlidingWindow(l,k))


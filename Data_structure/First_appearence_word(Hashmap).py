#给定一维数组，求数组中 从左往右 每个数字 第一次 出现的位置。如果是 第一次 出现则返回 -1。

#输入：[1,3,1,2,1]
#输出：[-1,-1,0,-1,0]
#解释：数字 1 出现了三次，第一次出现的位置是 0，所以除了 0 位置是 -1，其他数字 1 对应的位置答案均为 0。

from typing import List

class Solution:
    def find_left_repeat_num(self, nums: List[int]) -> List[int]:
        hashmap = {}
        resList = []
        for i,num in enumerate(nums):
            #if num exist in hashmap
            if num in hashmap:
                resList.append(hashmap[num])
            else:
                #reserve in dict
                hashmap[num] = i
                resList.append(-1)

        return resList


solution = Solution()
l = [1,3,1,2,1]
print(solution.find_left_repeat_num(l))
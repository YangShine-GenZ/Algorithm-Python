'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


'''

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        '''
        for(i):
            now = get_edge(nums[i])
            if (now<=edge):continue
            if (now>edge):
                for j: [edge:now]:
                    update_skip(nums[j])

        return skip[-1]
        '''

        n = len(nums)
        skip_num = [-1]*n
        edge = 0
        skip_num[0] = 0
        for i in range(n):
            now = i + nums[i]
            if now <= edge:
                continue
            else:
                for j in range(edge+1,now+1):
                    if j<n:
                        skip_num[j] = skip_num[i]+1
                edge = now


        #debug
        print(skip_num)

        return skip_num[-1]



s = Solution()
l = [2,3,0,1,4]


s.jump(l)


#print(s.jump(l))




'''
给定区间 intervalsi:[starti,endj]
找到每个interval最近的右区间

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]

'''

from typing import List
from bisect import bisect_left

def Binartsect_left(intervals:List[List[int]],x:int):

    left = 0
    right = len(intervals)-1
    while left<=right:
        mid = left+ int((right-left)/2)
        if intervals[mid][1] < x:
            left = mid+1
        if intervals[mid][1] > x:
            right = mid -1
        if intervals[mid][1] == x:
            right = mid - 1

    return left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
        for(len(l)):
            l[i].append(index)
        sorted(l[0])

        for(len(l)):
            //左边界
            index = bisect_left(l[i][0])
            list.append(l[index][2])
        '''

        res = [-1]*len(intervals)

        for i in range(len(intervals)):
            intervals[i].append(i)

        sorted_l = sorted(intervals,key= lambda x:x[0])
        #debug
        print(intervals)
        print(sorted_l)

        for start,end,index in sorted_l:
            #right_index = Binartsect_left(sorted_l,end)
            right_index = bisect_left(sorted_l,[end])
            if right_index < len(intervals):
                res[index] = sorted_l[right_index][2]
        print(res)
        return res




s = Solution()
l = [[1,4],[3,4],[2,3]]
s.findRightInterval(l)




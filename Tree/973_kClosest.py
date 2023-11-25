'''
给定一个数组 points，其中points[i] = [xi, yi]表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。

这里，平面上两点之间的距离是欧几里德距离（√(x1- x2)2+ (y1- y2)2）。

你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。

输入：points = [[3,3],[5,-1],[-2,4]], k = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）


'''

from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i, (x, y) in enumerate(points):
            sq = -(x * x + y * y)
            heapq.heappush(heap, (sq, i))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        for i in range(len(heap)):
            index = heap[i][1]
            res.append(points[index])

        # debug
        print(res)
        return res
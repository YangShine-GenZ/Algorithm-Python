'''

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4]的中位数是 3。
例如arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5以内的答案将被接受。

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

利用大小堆进行处理


'''

import heapq


class MedianFinder:

    def __init__(self):
        self.q_min = []  # 小端堆 用来存储大于平均值的数
        self.q_max = []  # 大端堆 用来存储小于平均值的数
        # 默认q_min的个数 比 q_max的个数多 1
        '''
        if len(q_min==q_max): average = (q_min[0]+(-q_max[1]))/2
        else: average = q_min[0]


        '''

    def addNum(self, num: int) -> None:
        if len(self.q_max) + len(self.q_min) == 0:
            heapq.heappush(self.q_min, num)
            print("now q_min:",self.q_min)
            print("now q_max",self.q_max)
            return
        if len(self.q_max) + len(self.q_min) == 1:
            heapq.heappush(self.q_min, num)
            average = heapq.heappop(self.q_min)
            heapq.heappush(self.q_max, -average)
            print("now q_min:",self.q_min)
            print("now q_max",self.q_max)
            return

        if num <= -(self.q_max[0]):
            heapq.heappush(self.q_max, -num)
            if len(self.q_max) > len(self.q_min):
                average = heapq.heappop(self.q_max)
                heapq.heappush(self.q_min, -average)
        else:
            heapq.heappush(self.q_min, num)
            if len(self.q_min) > len(self.q_max) + 1:
                average = heapq.heappop(self.q_min)
                heapq.heappush(self.q_max, -average)

        # debug
        print("now q_min:",self.q_min)
        print("now q_max",self.q_max)

    def findMedian(self) -> float:
        if len(self.q_max) == 0 and len(self.q_min) == 0:
            print("No element!")
            return None
        if len(self.q_min) == len(self.q_max):
            print("average:", (self.q_min[0] + (-self.q_max[0])) / 2)
            return (self.q_min[0] + (-self.q_max[0])) / 2
        else:
            print("average:", self.q_min[0])
            return self.q_min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
medianFinder.findMedian() # 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
medianFinder.findMedian() # return 2.0
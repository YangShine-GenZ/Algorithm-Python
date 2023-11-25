#实现循环队列

class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [0 for i in range(k)]
        self.head = 0
        self.rear = 0
        self.size = 0
        self.maxsize = k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            print("Push false!")
            return False
        self.array[self.rear] = value
        self.rear+=1
        self.rear%=self.maxsize
        self.size+=1
        print("Push num:",value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            print("Pop false!")
            return False
        self.head+=1
        self.head%=self.maxsize
        self.size-=1
        print("Pop......")
        return True


    def Front(self) -> int:
        if self.size==0:
            return -1
        print("Print Front:",self.array[self.head])
        return self.array[self.head]

    def Rear(self) -> int:
        if self.size==0:
            return -1
        rear  = (self.head+self.size-1)%self.maxsize
        print("Print Rear:", self.array[rear])
        return self.array[rear]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.maxsize




circularQueue = MyCircularQueue(3) # 设置长度为 3
circularQueue.enQueue(1) # 返回 true
circularQueue.enQueue(2) # 返回 true
circularQueue.enQueue(3) # 返回 true
circularQueue.enQueue(4) # 返回 false，队列已满
circularQueue.Rear() # 返回 3
circularQueue.isFull() # 返回 true
circularQueue.deQueue() # 返回 true
circularQueue.enQueue(4) # 返回 true
circularQueue.Rear() # 返回 4


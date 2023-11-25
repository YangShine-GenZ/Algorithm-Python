'''
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

'''



class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        #debug
        print("push:",x)

    def pop(self) -> int:
        if self.empty():
            print("Empty! NO POP!")
        if len(self.s2)==0:
            while len(self.s1)>0:
                temp = self.s1.pop(-1)
                self.s2.append(temp)
        print("POP:",self.s2[-1])
        temp = self.s2.pop(-1)
        return temp

    def peek(self) -> int:
        if self.empty():
            print("Empty! NO TOP!")
        if(len(self.s2)==0):
            while(len(self.s1)>0):
                temp = self.s1.pop(-1)
                self.s2.append(temp)
        print("Peek：",self.s2[-1])
        return self.s2[-1]

    def empty(self) -> bool:
        #debug
        print(len(self.s1)+len(self.s2) == 0)
        return len(self.s1)+len(self.s2) == 0


myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek() # return 1
myQueue.pop() # return 1, queue is [2]
myQueue.empty() # return false
myQueue.peek() # return 1
myQueue.pop() # return 1, queue is [2]
myQueue.empty() # return false

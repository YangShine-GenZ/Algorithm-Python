#利用队列实现栈
#queue:  push q1.put()  pop q1.get()  size q1.qsize

import queue

class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        print("doing push:",x)
        self.q1.put(x)

    def pop(self) -> int:
        print("doing pop......")
        x = self.top()
        self.q1.get()
        self.q1,self.q2 = self.q2,self.q1
        return x



    def top(self) -> int:
        while self.q1.qsize()>1:
            res = self.q1.get()
            self.q2.put(res)
        res = self.q1.get()
        self.q1.put(res)
        print("get top:",res)
        return res




    def empty(self) -> bool:
        print("judging empty...")
        return (self.q1.qsize()+self.q2.qsize()==0)




myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top() # 返回 2
myStack.pop() # 返回 2
myStack.empty() # 返回 False





# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()